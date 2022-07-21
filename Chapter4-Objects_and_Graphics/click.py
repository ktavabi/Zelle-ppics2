#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""click.py"""
from graphics import GraphWin


def main():
    """get mouse click"""
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print("You clicked at:", p.getX(), p.getY())


main()
