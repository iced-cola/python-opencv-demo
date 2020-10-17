# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo4
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/16 12:21 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np


def do_thing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, do_thing)
cv2.createTrackbar('G', 'image', 0, 255, do_thing)
cv2.createTrackbar('B', 'image', 0, 255, do_thing)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'image', 0, 1, do_thing)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(0) == ord('q'):
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[::] = [b, g, r]
cv2.destroyAllWindows()
