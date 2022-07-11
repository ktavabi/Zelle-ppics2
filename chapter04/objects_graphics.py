#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   objects_graphics.py
@Time    :   2022/07/11 00:18:40
@Author  :   Kambiz Tavabi
@Version :   0.1
@Contact :   ktavabi@gmail.com
@License :   MIT License (C)Copyright 2022, Kambiz Tavabi
@Desc    :   PPIC-Zelle Chapter 4 solutions
'''

# %% [markdown]
# # Objectives
# - To understand the concept of objects and how they can be used to simplify programming
# - To become familiar with the various objects available in the graphics library.
# - To be able to create objects in programs and call appropriate methods to preform graphical computations.
# - To understand the fundamental concepts of computer graphics, especially the role of coordinate systems and coordinate transforms.
# - To understand how to work with both mouse- and text-based input in a graphical programming context.
# - To be able to write simple interactive graphics programs using the graphics library.

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>*Pixels is short for picture elements*</b> Use blue boxes (alert-info) for tips and notes.</div>
# 
# *In OO programming each object is an instance of some class*
# *Constructor operation is used to create new class instances as <class-name>(<param1>, <param2>, ....)

# %%
from typing import Text
import graphics
win = graphics.GraphWin()

# %%
win.close()

# %%
p = graphics.Point(50,60)
win = graphics.GraphWin()
p2 = graphics.Point(140, 100)
for point in [p, p2]:
    point.draw(win)

# %%
win = graphics.GraphWin('Shapes')
center = graphics.Point(100, 100)
circ = graphics.Circle(center=center, radius=30)
circ.setFill('red')
circ.draw(win)
label = graphics.Text(center, "Red Circle")
label.draw(win)
rect = graphics.Rectangle(graphics.Point(30, 30), graphics.Point(70, 70))
rect.draw(win)
line = graphics.Line(graphics.Point(20, 30), graphics.Point(180, 165))
line.draw(win)
oval = graphics.Oval(graphics.Point(20, 150), graphics.Point(180, 199))
oval.draw(win)
# %%
