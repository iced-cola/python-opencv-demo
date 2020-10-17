# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo3
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/17 5:30 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/17:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

img = cv2.imread('../imgs/pi.png', cv2.IMREAD_GRAYSCALE)
height, width = img.shape
M = cv2.getRotationMatrix2D((width / 2, height / 2), 270, 0.8)
result = cv2.warpAffine(img, M, dsize=None, dst=None, flags=cv2.BORDER_CONSTANT, borderValue=1)

while 1:
    cv2.imshow('result', result)
    cv2.imshow('image', img)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
