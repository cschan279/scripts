#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: TrC
"""
import time
def count(num):
    x = input('Ready?')
    t1 = time.time()
    for i in range(num):
        x = input(str(i))
    t2 = time.time()
    dt = t2 - t1
    fq = dt / num
    return dt, fq
