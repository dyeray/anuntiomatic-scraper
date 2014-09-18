from selenium import webdriver
from PIL import Image
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (NoSuchElementException,
                                        NoAlertPresentException)
import unittest  # , time, re
from easygui import enterbox
import urllib2


class Anuntios(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://backoffice.anuntiomatic.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_anuntios(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("Juanitovalderrama")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("njd#HW73p2")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_xpath(
            "//div[2]/div/div/div/ul/li[16]/a/span").click()
        captcha = driver.find_element_by_xpath("//img[starts-with(@src, 'captcha.php')]")
        location = captcha.location
        size = captcha.size
        driver.save_screenshot('img.png')
        img = Image.open('img.png')
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        img = img.crop((left, top, right, bottom))
        img.save('img.png')
        import pdb; pdb.set_trace()
        #url = 'http://backoffice.anuntiomatic.com/captcha.php?cod=1'
        #f = urllib2.urlopen(url)
        #with open("img.png", "wb") as code:
        #    code.write(f.read())
        #reply = enterbox(image="img.png")
        driver.find_element_by_id("respuesta").clear()
        driver.find_element_by_id("respuesta").send_keys("99611")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        driver.find_element_by_link_text("http://pacsdelpenedes.anuntiomatic.es/ad/view/servicios/241815688/calculadora-solar--oro-en-teletienda-anuntiomatic").click()
        driver.find_element_by_link_text(
            "Pulse aqui para generar sus BonoMatics").click()
        driver.find_element_by_css_selector(
            "div[alt=\"Close Advertising\"]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
