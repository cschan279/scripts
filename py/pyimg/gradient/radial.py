#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
import numpy as np
from random import shuffle, randint
import cv2

#w, h = 1920,1080
w, h = 800,600


a = np.fromfunction(lambda i,j,k:(i*j)*(255)//(w*h), (h,w,1))
b = np.fromfunction(lambda i,j,k:((h-i)*j)*(255)//(w*h), (h,w,1))
c = np.fromfunction(lambda i,j,k:(i*(w-j))*(255)//(w*h), (h,w,1))
d = np.fromfunction(lambda i,j,k:((h-i)*(w-j))*(255)//(w*h), (h,w,1))

ls = [a,b,c,d]
shuffle(ls)

t = (ls[0],ls[1],ls[2])

im = np.concatenate(t, axis=2).astype(np.uint8)


cv2.imshow('test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
