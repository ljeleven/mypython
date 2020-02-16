#__author:"longjin"
#date:  2019/7/12
# -*- coding: UTF-8 -*-

import os
from PIL import Image

path = 'C:/Users/lj/Desktop/image/3/'
dirs = os.listdir(path)
ims = []
# for fn in dirs:
#     for k in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
#         if fn.endswith(k+'.jpg'):
#             ims.append(Image.open(path + fn))
ims = [Image.open(path + fn) for fn in dirs if fn.endswith('.jpg')]
print(ims)
width, height = ims[0].size
x_s = 820
y_s = 1160
#创建A4大小的图
result = Image.new(ims[0].mode, (2479, 3508))
#enumerate 枚举
for i, im in enumerate(ims):
    for j in range(3):
        #修改图片大小  Image.ANTIALIAS高质量
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        #图片放到result上
        result.paste(out, box=(j * x_s+6, i * y_s+9))





result.save('C:/Users/lj/Desktop/image/3/result.png')