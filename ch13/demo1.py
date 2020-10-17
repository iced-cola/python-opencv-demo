# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo1
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/16 10:50 下午
   Description :  颜色空间转换
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

file = "../imgs/pi.png"

cap = cv2.VideoCapture(0)

while 1:
    # 读取帧
    ret, frame = cap.read()
    # 转换到hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # 设置阀值
    lower_blue = (110, 50, 50)
    upper_blue = (130, 255, 255)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
