# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo1
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/16 10:34 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

file1 = "../imgs/kanna.jpg"
file2 = "../imgs/pi.png"

print(cv2.getTickFrequency())

img1 = cv2.imread(file1)
img2 = cv2.imread(file2)
img1 = img1[100:300]
img2 = img2[100:300]

dst = cv2.addWeighted(img1, 0.3, img2, 0.7, gamma=1)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
