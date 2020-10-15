# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo1
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/15 8:08 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/15:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import numpy as np
import cv2

image = "../imgs/pi.png"

img = cv2.imread(image, cv2.COLOR_GRAY2RGB)

# 划线
cv2.line(img, (0, 0), (200, 200), (255, 0, 0), 5)

# 画一个矩形
cv2.rectangle(img, (100, 100), (400, 400), (255, 100, 100), thickness=5, lineType=cv2.LINE_AA)

# 画一个圆形
cv2.circle(img, (200, 200), 40, (20, 100, 200), thickness=3, lineType=cv2.LINE_8)

# 画一个椭圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# 画一个多边形
points = np.array([[100, 50], [200, 300], [70, 200], [50, 100]], np.int32)
points = points.reshape((-1, 1, 2))
cv2.polylines(img, [points], True, (200, 100, 0), 3, lineType=cv2.LINE_AA, shift=2)

# 在图片上添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "live camera", (30, 450), font, 2, (25, 25, 25), thickness=1, lineType=cv2.LINE_AA)

cv2.imshow('image', img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
