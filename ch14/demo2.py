# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo2
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/17 5:13 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/17:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

img = cv2.imread("../imgs/pi.png", cv2.IMREAD_GRAYSCALE)
height, width = img.shape
# 平移矩阵x=100,y=50
M = np.float32([[1, 0, 100], [0, 1, 50]])
result = cv2.warpAffine(img, M, (width, height), dst=None, borderMode=cv2.BORDER_REFLECT, borderValue=3)

while 1:
    cv2.imshow('result', result)
    cv2.imshow('image', img)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
