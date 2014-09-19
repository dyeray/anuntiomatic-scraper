# -*- encoding: UTF-8 -*-

from selenium import webdriver
from PIL import Image
#from selenium.common.exceptions import (NoSuchElementException,
#                                        NoAlertPresentException)
#import unittest
#from easygui import enterbox
import re
from random import randrange
import time
from selenium.common.exceptions import NoAlertPresentException
from captcha import AnuntiomaticCaptcha


class Anuntios:

    def run(self):
        while True:
            try:
                self._make_ads()
            except KeyboardInterrupt:
                self.driver.quit()
                exit()
            except Exception as e:
                print e
                self.driver.quit()
                self._make_ads()

    def _make_ads(self):

        # Init selenium
        self.driver = webdriver.Firefox()
        driver = self.driver
        self.driver.implicitly_wait(10)
        self.base_url = "http://backoffice.anuntiomatic.com/"

        # Login
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("Juanitovalderrama")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("njd#HW73p2")
        driver.find_element_by_css_selector("button.btn.btn-primary").click()
        while True:
            time.sleep(2)
            driver.get('http://backoffice.anuntiomatic.com/publicar.php?op=1')
            captcha = driver.find_element_by_xpath(
                "//img[starts-with(@src, 'captcha.php')]")
            location = captcha.location
            size = captcha.size
            driver.save_screenshot('img.png')
            img = Image.open('img.png')
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            img = img.crop((left, top, right, bottom))
            captcha_text = AnuntiomaticCaptcha(img).get_text()
            #captcha_text = enterbox(image="img.png")
            driver.find_element_by_id("respuesta").clear()
            driver.find_element_by_id("respuesta").send_keys(captcha_text)
            driver.find_element_by_css_selector(
                "button.btn.btn-primary").click()
            driver.find_element_by_xpath(
                "//a[starts-with(@href, 'veranuncio.php')]").click()
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(61 + randrange(3))
            driver.find_element_by_link_text(
                "Pulse aqui para generar sus BonoMatics").click()
            driver.get(re.sub(r'adf\.ly/[0-9]*/(banner/)?', "",
                       driver.current_url))
            try:
                alert = driver.switch_to_alert()
                alert.accept()
            except NoAlertPresentException:
                pass
            time.sleep(1)
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

if __name__ == "__main__":
    Anuntios().run()
