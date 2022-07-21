# Objectives

- To understand the concept of objects and how they can be used to simplify programming
- To become familiar with the various objects available in the graphics library
- To be able to create objects in programs and call appropriate methods to preform aphical computations
- To understand the fundamental concepts of computer graphics, especially the role of ordinate systems and coordinate transforms
- To understand how to work with both mouse- and text-based input in a graphical ogramming context
- To be able to write simple interactive graphics programs using the graphics library

### Notes

- In OO programming each object is an instance of some class
- Constructor operation is used to create new class instances as ```<class-name>(<param1>, <param2>, ....)```
- In _event-driven_ OO programming an event is an object that encapsulates data about what just happend.

## Summary

- An object is a computational entity that combines data and operations. Objects know stuff and can do stuff. An object's data is stored in _instance variables_, and its operations are called _methods_.
- Every object is an instance of some class. It is the class that determines what methods an object will have. An instance is created by calling a _constructor method_.
- An object's attributes are accessed via _dot_ notation. Generally computations with objects are performed by calling on an object's methods. Accessor methods return information about the instance variables, e.g. `point.getX()` is a `Point` class accessor method `getX()`. Mutator methods change the value(s) of instance variables.
- An important consideration in graphical programming is the choice of an appropriate coordinate system. The graphics library provides a way of automating certain coordinate transformations. The graphics module provides a number of classes for graphics programming. A `GraphWin` is an object that represents a window on the screen for displaying graphics. Various graphical objects such as `Point`, `Line`, `Circle`, `Rectangle`, `Oval`, `Polygon`, and `Text`, may be drawn in a `GraphWin`. Users can interact with a `GraphWin` by mouse clicks or text input into `Entry` box.
- The situation where two variables refer to the same object is called _aliasing_. It can sometimes cause unexpected results. Use of the `clone` _mutator method_ in the graphics library can help prevent aliasing.

## Exercises

#### True/False

1. False. Using graphics.py allows graphics to be drawn into a Python shell window. Graphics appear in new window.
2. True
3. True. Pixel is short for picture elements
4. False. It's called a _constructor_
5. True.
6. False. It moves the x coordinate by 10 points and the y coordinate by 20 points.
7. True
8. False. The clone method returns a copy of a graphics object.
9. False. It is the default parameter. However, it is possible to pass a different title.
10. False. It is getMouse() method.

#### Multiple Choice

1. (D) (accessor)
2. (B) (mutator)
3. (D) (Rectangle)
4. (C) (win.setcoords(0, 0, 10, 10))
5. (D) (Line(Point(2,3), Point(4,5)))
6. (C) (shape.draw(win))
7. (D) (abs(p1.getX() - p2.getY()))
8. (B) (Entry)
9. (A) (GUI)
10. (B) (cyan)

### Discussion

1. Consider an ordinary light bulb, as a programming object it can return a `boolean` data type representing it's state (on/off), and contain data attributes representing to ```[<luminasence> -> int, <type> -> str, <watts> -> int]```.

2. make a point at x=130, y=130
    1. set c equal to a Circle class with center at a Point at x=30, y=40 with a radius of 30 pixels. Set the fill color to blue and set outline color to red.
    2. set r equal to a Rectancle class instance with diagonal vertices LLt:(x=20, y=40) and URt:(x=40, y=40). Set the the fill color to green and set border lw to 3 px.
    3. set l equal to Line class instance between Point(100, 100) and Point(100, 200). Set line color to dark red and arrow head at starting point.
    4. Construct an Oval in a bounding box between Point(50, 50) and Point(60, 100)
    5. Construct an orange filled polygon with four vertices.
    6. Construct a Text object anchored at Point(100, 100) saying "Hellow World!" string. Set the font type to Courier, text size to 16 and italicize.

3. Construct a GraphWin object, in it construct a Circle with radius 20 px centered at Point(50,50), set the fill color and border color to red, and draw the SHAPE. Then in a for-loop prompt user for a mouse click inside win and construct a Point class for the click. Get the Circle SHAPE center as c and calculate the horizontal (dx) & vertical (dy) distances between mouse click coordinate and SHAPE center. Translate SHAPE center to calculated distances (dx, dy). Repeat for-loop 10 times. Close the win.

### Programming Exercises

1. Alter E.g. program to draw different shape and behave differently.

    ```python
    from graphics import GraphWin, Rectangle, Point, Text

    def main():
        win = GraphWin("Window I", 800, 800)
        # 1(a) construct square instead of circle
        shape = Rectangle(Point(50,50), Point(100,100))
        shape.setOutline("red")
        shape.draw(win)
        op = shape.getCenter()
        for ii in range(10):
            # 1(b) construct new shape at mouse location
            np = win.getMouse()
            ns = Rectangle(op, np)
            ns.draw(win)
            op = ns.getCenter()
        # 1(c) print msg at center of last new shape, wait for click on win, close win 
        txt = Text(op, "Click Again to quit")
        txt.setFace("courier")
        txt.setSize(12)
        txt.setStyle("bold")
        txt.draw(win)
        win.getMouse()
        win.close()


    main()
    ```

2. Draw a yellow circle, concentrically surrounded by four rings of red, blue, black, white.

    ```python
    from graphics import *

    def main():
        """draw concentric circles with scaled radii"""
        win = GraphWin("Bullseye", 800, 800)
        rad_yellow = 50  # px
        scaler = 5
        for color in ["white", "black", "blue", "red", "yellow"]:
            circle = Circle(Point(400, 400), rad_yellow * scaler)
            circle.setFill(color)
            scaler -= 1
            circle.draw(win)
        txt = Text(Point(400, 400), "Click Again to quit")
        txt.setFace("courier")
        txt.setSize(12)
        txt.setStyle("bold")
        txt.draw(win)
        win.getMouse()
        win.close()


    main()
    ```
