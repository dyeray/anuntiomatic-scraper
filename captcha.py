# -*- encoding: UTF-8 -*-

from PIL import Image
import pytesseract
import re

image = Image.open('img.png')
solid = Image.new("RGB", image.size, (255, 255, 255))
solid.paste(image)
pixdata = solid.load()
for y in xrange(solid.size[1]):
    for x in xrange(solid.size[0]):
        if (pixdata[x, y][0] >= 5 or
                pixdata[x, y][1] >= 5 or pixdata[x, y][2] >= 65):
            pixdata[x, y] = (255, 255, 255)
captcha_text = re.sub("[^0-9]", "", pytesseract.image_to_string(solid))
print(captcha_text)
solid.save('solid.bmp')
