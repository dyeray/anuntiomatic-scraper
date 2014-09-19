# -*- encoding: UTF-8 -*-

from PIL import Image
import pytesseract
import re


class AnuntiomaticCaptcha:

    def __init__(self, image):
        self.image = image

    def _preprocess(self):
        image = Image.new("RGB", self.image.size, (255, 255, 255))
        image.paste(self.image)
        pixdata = image.load()
        for y in xrange(image.size[1]):
            for x in xrange(image.size[0]):
                if (pixdata[x, y][0] >= 5 or
                        pixdata[x, y][1] >= 5 or pixdata[x, y][2] >= 65):
                    pixdata[x, y] = (255, 255, 255)
        return image

    def save_processed(self, path):
        image = self._preprocess()
        image.save(path)

    def save(self, path):
        self.image.save(path)

    def get_text(self):
        solid = self._preprocess()
        return re.sub("[^0-9]", "",
                      pytesseract.image_to_string(solid))
