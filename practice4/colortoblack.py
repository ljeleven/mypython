#__author:"longjin"
#date:  2019/7/11
# -*- coding: UTF-8 -*-

import os
from PIL import Image

path = 'C:/Users/lj/Desktop/image/'
dirs = os.listdir(path)
for file in dirs:
    img1 = Image.open(path+file)
    img1 = img1.convert('L')
    threshold = 220
    table = []

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    img1 = img1.point(table, '1')
    img2 = img1.convert('RGBA')
    width, height = img2.size

    for h in range(height):
        for w in range(width):
            data = (img2.getpixel((w, h)))
            print(data)
            if data[0] >= 250:
                img2.putpixel((w, h), (255, 255, 255, 0))

    img2.save('C:/Users/lj/Desktop/image/' + file.split('.')[-2]+'.png')