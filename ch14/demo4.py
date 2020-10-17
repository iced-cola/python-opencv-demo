# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo4
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/17 5:40 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/17:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("../imgs/pi.png")
rows, cols, ch = img.shape
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
plt.subplot(121, plt.imshow(img), plt.title('Input'))
plt.subplot(121, plt.imshow(img), plt.title('Output'))
plt.show()
