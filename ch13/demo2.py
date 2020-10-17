# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo2
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/17 4:29 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/17:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    if cv2.waitKey(0) == ord('q'):
        break
cv2.destroyAllWindows()
