# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     地膜
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/17 4:46 下午
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
result1 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
result2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
result3 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# height, width = img.shape[0:2]
# result = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
while 1:
    cv2.imshow('INTER_CUBIC', result1)
    cv2.imshow('INTER_AREA', result2)
    cv2.imshow('INTER_LINEAR', result3)
    # cv2.imshow('image', img)
    if cv2.waitKey(4) == ord('q'):
        break
cv2.destroyAllWindows()
