#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
import numpy as np
from random import shuffle, randint
import cv2

w, h = 1920,1080
#w, h = 800,600
rg = 50

x = np.fromfunction(lambda i,j,k:j*(255-rg*2)//w+rg, (h,w,1))#.astype(np.uint8)
rx = np.random.randint(rg, size=(h,w,1)) - rg//2
x = (x + rx)
x = x.astype(np.uint8)

y = np.fromfunction(lambda i,j,k:i*(255-rg*2)//h+rg, (h,w,1))#.astype(np.uint8)
ry = np.random.randint(rg, size=(h,w,1)) - rg//2
y = (y + ry)
y = y.astype(np.uint8)



z = np.ones((h,w,1), dtype=np.uint8)*randint(0,255)

t = [z,x,y]
shuffle(t)

im = np.concatenate(tuple(t), axis=2)
print(im.shape)

cv2.imshow('test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('a.jpg', im)
