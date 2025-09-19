import turtle as t

t.shape('turtle')
t.bgcolor('black')
t.color('yellow')

t.penup()
t.goto(100, 100)
t.pendown()

angle = 89

for x in range(2000):
    t.forward(x)
    t.left(angle)
