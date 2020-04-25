#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
import cv2
import numpy as np
from random import randint
import math

width, height = 800,600
#width, height = 1920,1080
s = 100

c = (width//2, height//2)
color = [0,0,255]

im = np.ones((height,width,3), dtype=np.uint8)*255
sAng = 0
sPt = c


def calcoor(ang, wd, hd, ctr):
    #r = math.sqrt(wd*wd+hd*hd)/math.sqrt(2)
    x = math.cos(ang*math.pi/180)*wd
    y = math.sin(ang*math.pi/180)*hd
    pos = (int(ctr[0]+x), int(ctr[1]+y))
    return pos
    



for i in range(s*2):
    eAng = randint(0,360)
    
    w = width * i // s // 2
    h = height * i // s // 2
    
    ePt = calcoor(sAng, w,h, c)
    
    im = cv2.ellipse(im, c, (w, h), 0, sAng,eAng, tuple(color), 2)
    sAng = eAng
    im = cv2.line(im, sPt, ePt, color, 2)
    
    ch = randint(0,2)
    color[ch] += randint(0,20)
    color[ch] = color[ch] if color[ch] <= 255 else color[ch]-255
        
    sPt = calcoor(eAng, w,h, c)




cv2.imshow('test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
