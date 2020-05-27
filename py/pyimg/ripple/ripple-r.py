#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
import numpy as np
import cupy as cp
from random import shuffle, randint
import cv2

w, h = 1920,1080
w, h = 800,600



def rip(ax, ay, cx, cy, m=10):
    cax, cay = cp.asarray(ax), cp.asarray(ay)
    car2 = cp.square(cax - cx) + cp.square(cay - cy)
    cvec = cp.square(cp.cos(cp.sqrt(car2)/m))*255
    vec = cp.asnumpy(cvec)
    return vec


t = []
for _ in range(3):
    fqt = (w//4, h//4)
    tqt = (fqt[0]*3, fqt[1]*3)
    cpt = (randint(fqt[0], tqt[0]), randint(fqt[1], tqt[1]))
    m = randint(5,15)
    a = np.fromfunction(lambda i,j,k:rip(j, i, cpt[0], cpt[1], m), (h,w,1))
    t.append(a)


#ls = [a,b,c,d]
#shuffle(ls)

#t = (ls[0],ls[1],ls[2])


im = np.concatenate(tuple(t), axis=2).astype(np.uint8)


cv2.imshow('test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
