#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : fibonacci-malformed.py
'''Purpose : Intro sth                                 '''
# Creation Date : 1395839444
# Last Modified :
# Release By : Doom.zhou
def fib(n):
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a+b
fib(42)

