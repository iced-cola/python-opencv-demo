# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     canddy
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/19 10:26 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/19:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../imgs/test.jpeg")

cv2.namedWindow('image')


def do_nothing(x):
    pass


cv2.createTrackbar('minVal', 'image', 0, 500, do_nothing)
cv2.createTrackbar('maxVal', 'image', 0, 500, do_nothing)

while 1:
    minVal = cv2.getTrackbarPos('minVal', 'image')
    maxVal = cv2.getTrackbarPos('maxVal', 'image')
    if minVal > maxVal:
        cv2.setTrackbarPos('minVal', 'image', maxVal)
    dst = cv2.Canny(img, minVal, maxVal)
    cv2.imshow('image', dst)
    if cv2.waitKey(5) == ord('q'):
        break
cv2.destroyAllWindows()
