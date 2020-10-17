# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
-------------------------------------------------
   File Name:     demo5
   Author:        zhulongkun20@gmail.com
   Date:          2020/10/16 12:39 下午
   Description :   
-------------------------------------------------
   Change Activity:
                   2020/10/16:
-------------------------------------------------
"""

__author__ = 'zhulongkun20@gmail.com'

import cv2
import numpy as np


def do_nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (r, g, b), thickness=2, lineType=cv2.LINE_AA)


def draw_rectangle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img, (100, 100), (x, y), (r, g, b), thickness=4, lineType=cv2.LINE_AA)


def draw_line(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.line(img, (200, 200), (x, y), (r, g, b), thickness=6, lineType=cv2.LINE_AA)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, do_nothing)
cv2.createTrackbar('G', 'image', 0, 255, do_nothing)
cv2.createTrackbar('B', 'image', 0, 255, do_nothing)
switch = "0:circle\n1:rectangle\n2:line"
cv2.createTrackbar(switch, 'image', 0, 2, do_nothing)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        cv2.setMouseCallback('image', draw_circle)
    elif s == 1:
        cv2.setMouseCallback('image', draw_rectangle)
    else:
        cv2.setMouseCallback('image', draw_line)
cv2.destroyAllWindows()
