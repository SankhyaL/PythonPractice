from turtle import*
from random import randint

pencil = Turtle()

for i in range(4):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color1=(r/255, g/255, b/255)

    x = randint(-200,200)
    y = randint(-200,200)

    pencil.up()
    pencil.goto(x,y)
    pencil.down()

    pencil.color(color1)
    pencil.begin_fill()
    for i in range(4):
        pencil.fd(100)
        pencil.rt(90)
    pencil.end_fill()

done()
