Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import Turtle
>>> import math
>>> def drawCircle(t, x_center, y_center, radius):
...     distance = (2.0 * math.pi * radius) / 120.0
...     t.penup()
...     t.goto(x_center, y_center - radius)
...     t.pendown()
...     for _ in range(120):
...         t.forward(distance)
...         t.left(3)
... 
...         
>>> def main():
...     t = Turtle()
...     drawCircle(t, 50, 75, 100)
... 
...     
>>> if __name__ == "__main__":
...     main()
... 
...     
