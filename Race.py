import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.shape('turtle')
t1.color('purple')
t1.speed(1)

t2.shape('turtle')
t2.color('blue')
t2.speed(1)

t3.shape('turtle')
t3.color('red')
t3.speed(1)

# Let turtle move upwards
t1.left(90)
t1.write(t1.position())

t2.penup()
t2.goto(200, 0)
t2.left(90)
t2.pendown()
t2.write(t2.position())

t3.penup()
t3.goto(-200, 0)
t3.left(90)
t3.pendown()
t3.write(t3.position())

winner = ''

# Start move turtle at a random pace
for i in range(100):
    t1.forward(random.randint(0, 5))
    t2.forward(random.randint(0, 5))
    t3.forward(random.randint(0, 5))
    if winner == '':
        if t1.ycor() >= 100:
            winner = 't1'
            t1.write('i am first reach 100 pixel')
        if t2.ycor() >= 100:
            winner = 't2'
            t2.write('i am first reach 100 pixel')
        if t3.ycor() >= 100:
            winner = 't3'
            t3.write('i am first reach 100 pixel')

t1.write(t1.position())
t2.write(t2.position())
t3.write(t3.position())

turtle.done()