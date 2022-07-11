#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   solutions.py
@Time    :   2022/07/11 00:18:40
@Author  :   Kambiz Tavavi 
@Version :   0.1
@Contact :   ktavabi@gmail.com
@License :   MIT License (C)Copyright 2022, Kambiz Tavabi
@Desc    :   PPIC-Zelle Chapter 4 solutions
'''

from graphics import * 
mywin = GraphWin("ponies!!", 600, 500)
mywin.setBackground("lightblue")
click = mywin.getMouse()   # will pause here until mouse clicked in graph win
print(click)
key = mywin.getKey()   # will pause here until key pressed in graph win
print(key)