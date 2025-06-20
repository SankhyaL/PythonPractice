from turtle import*

pencil = Turtle()

colors = ["red", "yellow", "purple", "orange", "blue", "light green"]

for i in range(6):
    pencil.color(colors[i])
    pencil.width(5)
    pencil.fd(100)
    pencil.rt(60)

done()
