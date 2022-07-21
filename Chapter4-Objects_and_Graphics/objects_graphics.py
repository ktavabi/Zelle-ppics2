#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   objects_graphics.py
@Time    :   2022/07/11 00:18:40
@Author  :   Kambiz Tavabi
@Version :   0.1
@Contact :   ktavabi@gmail.com
@License :   MIT License (C) Copyright 2022, Kambiz Tavabi
@Desc    :   PPIC-Zelle Chapter 4 solutions
"""

# %% [markdown]
# # Objectives
# - To understand the concept of objects and how they can be used to simplify programming
# - To become familiar with the various objects available in the graphics library.
# - To be able to create objects in programs and call appropriate methods to preform graphical computations.
# - To understand the fundamental concepts of computer graphics, especially the role of coordinate systems and coordinate transforms.
# - To understand how to work with both mouse- and text-based input in a graphical programming context.
# - To be able to write simple interactive graphics programs using the graphics library.

#%% [markdown]
# ### Notes
# - Pixels is short for picture elements.
# - In OO programming each object is an instance of some class.
# - Constructor operation is used to create new class instances as <class-name>(<param1>, <param2>, ....)
# -

# %%
import graphics

win = graphics.GraphWin()

# %%
win.close()

# %%
p = graphics.Point(50, 60)
win = graphics.GraphWin()
p2 = graphics.Point(140, 100)
for point in [p, p2]:
    point.draw(win)

# %%
win = graphics.GraphWin("Shapes")
center = graphics.Point(100, 100)
circ = graphics.Circle(center=center, radius=30)
circ.setFill("red")
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
from graphics import GraphWin, Point, Rectangle, Text


def main():
    """plot growth of 10-year investment"""
    print("This program plots the growoth of a 10-year investment.")
    # get principal and apr
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))

    # create figure window with left axis
    win = GraphWin("Investment growth", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), " 0.0K").draw(win)
    Text(Point(20, 180), " 2.5K").draw(win)
    Text(Point(20, 130), " 5.0K").draw(win)
    Text(Point(20, 80), " 7.5K").draw(win)
    Text(Point(20, 30), " 10.0K").draw(win)

    # draw bar for init principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # draw bars for successive yrs
    for yr in range(1, 11):
        # calc value for next year
        principal = principal * (1 + apr)
        # draw next bar
        xll = yr * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()


main()

# %%
