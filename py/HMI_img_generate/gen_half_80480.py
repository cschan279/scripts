#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: troyc
"""
import numpy as np
import cv2

#@#@#@#@#@#@#@# Config #@#@#@#@#@#@#@#
font1 = cv2.freetype.createFreeType2()
font1.loadFontData('./arial.ttf',0)
font2 = cv2.freetype.createFreeType2()
font2.loadFontData('./times.ttf',0)

ft1 = cv2.FONT_HERSHEY_COMPLEX
ft2 = cv2.FONT_HERSHEY_COMPLEX
x1, x2 = 200, 600
y1, y2 = 100, 400
c1 = (200,240)
c2 = (600,240)
radius = 75
scale1, thick1 = 1.5,3
color1 = (0,0,0)
scale2, thick2 = 1,2
color2 = (0,0,0)
#@#@#@#@#@#@#@# Config #@#@#@#@#@#@#@#

def textimg(img, text, ft, ctrX, ctrY, 
            scale, thick, color):
    if isinstance(ft, int): 
        t_size = cv2.getTextSize(text,ft,scale,thick)[0]
    else:
        t_size = ft.getTextSize(text, scale, thick)[0]
    offset = (t_size[0]//2, t_size[1]//2)
    pos = (ctrX - offset[0], ctrY + offset[1])
    if isinstance(ft, int): 
        cv2.putText(img,text,pos,ft,scale,color,thick, 8, False)
    else:
        ft.putText(img, text, pos, scale, color, 
                   thick, 8, True)
    return img



def text2img(tx1, tx2, cl1, cl2):
    img = np.ones((480,800,3),np.uint8)*150
    img = textimg(img, tx1[0], ft1, x1, y1, scale1, thick1, color1)
    img = textimg(img, tx1[1], ft2, x1, y2, scale2, thick2, color2)
    cv2.circle(img, c1, radius, cl1[0], -1)
    cv2.circle(img, c1, radius, cl1[1], 3)
    img = textimg(img, tx2[0], ft1, x2, y1, scale1, thick1, color1)
    img = textimg(img, tx2[1], ft2, x2, y2, scale2, thick2, color2)
    cv2.circle(img, c2, radius, cl2[0], -1)
    cv2.circle(img, c2, radius, cl2[1], 3)
    return img
    
tx = [('Vacant',' '),
      ('Connected', 'Press START'),
      ('Charging', 'Press STOP to leave'),
      ('Stopped', 'Unplug the cable'),
      ('Error', ' ')]
#BGR
color = [((0,255,0),(0,127,0)),
         ((0,255,255),(0,127,127)),
         ((255,0,0),(127,0,0)),
         ((255,0,0),(127,0,0)),
         ((0,0,255),(0,0,127))]

count = 1
pat = 'img/{:02d}_{}_{}.jpg'
for i in range(5):
    for j in range(5):
        img = text2img(tx[i], tx[j], color[i], color[j])
        fname = pat.format(count, tx[i][0],tx[j][0])
        print(fname)
        cv2.imwrite(fname, img)
        count += 1


#img = text2img(('Connected', 'Press Start'), ('Charging', 'Press Stop'), 
               #((255,0,0), (127,0,0)), ((0,255,255), (0,127,127)))

#cv2.imshow('x',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite('x.jpg',img)
