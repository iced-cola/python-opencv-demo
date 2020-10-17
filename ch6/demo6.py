# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo6
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/16 12:57 下午
   Description :  打印图像的属性
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

file = "../imgs/pi.png"

img = cv2.imread(file)
print(img.size)
print(img.dtype)

img[:, :, 2] = 0

# b, g, r = cv2.split(img)
# print(b, g, r)
#
# eyes = img[200:250, 300:350]
#
# img[100:150, 200:250] = eyes

cv2.imshow('image', img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
