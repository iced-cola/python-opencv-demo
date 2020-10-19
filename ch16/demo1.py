# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo1
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/19 9:51 下午
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

img = cv2.imread("../imgs/pi.png")
K = np.ones([5, 5], np.float32) / 25
dst = cv2.filter2D(img, -1, K)
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

# dst = cv2.blur(img, (3, 3))

# dst = cv2.GaussianBlur(img, (5, 5), 0)

# dst = cv2.medianBlur(img, 5)

# dst = cv2.bilateralFilter(img, 9, 75, 75)

# plt.subplot(121), plt.imshow(img), plt.title("原图")
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(dst), plt.title("平滑之后的图")
# plt.xticks([]), plt.yticks([])
# plt.show()
