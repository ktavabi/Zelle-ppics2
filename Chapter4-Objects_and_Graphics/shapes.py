#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''shape.py'''

import graphics

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
input("Press <Enter> to quit.")
