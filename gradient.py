#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

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



def grad(x, y, z, w, h):
    if z == 0:
        
