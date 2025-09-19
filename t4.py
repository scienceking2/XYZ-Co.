import turtle as t
import random

t.shape('turtle')
t.speed(0)

for x in range(10):
    a = ramdom.randint(1, 360)
    t.setheading(a)
    t.forward(100)
