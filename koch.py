Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from turtle import Turtle
>>> def draw_koch_segment(t, distance, angle, level):
...     if level == 0:
...         t.forward(distance)
...     else:
...         distance = distance / 3.0
...         draw_koch_segment(t, distance, angle, level - 1)
...         t.left(60)
...         draw_koch_segment(t, distance, angle, level - 1)
...         t.right(120)
...         draw_koch_segment(t, distance, angle, level - 1)
...         t.left(60)
...         draw_koch_segment(t, distance, angle, level - 1)
... 
...         
>>> def draw_koch_snowflake(t, distance, level):
...     for i in range(3):
...         draw_koch_segment(t, distance, 0, level)
...         t.right(120)
... 
...         
>>> def main():
...     t = Turtle()
...     t.hideturtle()
...     t.penup()
...     t.goto(-150, 86.6)
...     t.pendown()
...     t.pencolor("blue")
...     level = 3
...     draw_koch_snowflake(t, 300, level)
... 
...     
>>> if __name__ == "__main__":
...     main()
... 
...     
