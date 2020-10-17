# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo5
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/17 5:49 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/17:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

img = cv2.imread("../imgs/pi.png")
flip_img = cv2.flip(img, 50)

while 1:
    cv2.imshow('image', img)
    cv2.imshow('flip_img', flip_img)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
