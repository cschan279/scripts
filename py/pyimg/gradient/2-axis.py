#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from random import randint
import cv2
"""
Examples

>>>
>>> np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int)
array([[ True, False, False],
       [False,  True, False],
       [False, False,  True]])
>>>
>>> np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
array([[0, 1, 2],
       [1, 2, 3],
       [2, 3, 4]])
"""
#w, h = 1920,1080
w, h = 800,600

x = np.fromfunction(lambda i,j:j*(255-rg*2)//w, (h,w))
x = np.expand_dims(x,axis=2).astype(np.uint8)

y = np.fromfunction(lambda i,j:i*(255-rg*2)//h, (h,w))
y = np.expand_dims(y,axis=2).astype(np.uint8)


z = np.ones((h,w,1), dtype=np.uint8) * 255



im = np.concatenate((z,x,y), axis=2)
print(im.shape)

cv2.imshow('test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
