#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
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



x = np.fromfunction(lambda i,j:j//600*255, (600,800), dtype=np.uint8)

#x = x * (255 // 300)

x = np.expand_dims(x,axis=2)
y = np.fromfunction(lambda i,j:i//800*255, (600,800), dtype=np.uint8)
#y = y * (255 //400)
y = np.expand_dims(y,axis=2)
z = np.ones((600,800,1), dtype=np.uint8) * 255


im = np.concatenate((x,y,z), axis=2)
print(im.shape)

print(*x[0])

cv2.imshow('test', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
