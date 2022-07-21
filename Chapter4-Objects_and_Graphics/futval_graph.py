#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''futval_graph.py'''
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
