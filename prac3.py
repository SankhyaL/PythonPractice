from turtle import*

pencil = Turtle()

def square(p, size, color):
    p.color(color)
    p.begin_fill()
    for i in range(4):
        p.forward(size)
        p.right(90)
    p.end_fill()

def circle(p, radius, color):
    p.color(color)
    p.begin_fill()
    p.circle(radius)
    p.end_fill()

def pentagon(p, size, color):
    p.color(color)
    p.begin_fill()
    for i in range(5):
        p.forward(100)
        p.left(72)
    p.end_fill()

start = input("square/circle/pentagon: ").lower()

while start != "stop":
    if start == "square":
        size = int(input("Enter a size: "))
        color = input("Enter a color: ")
        square(pencil, size, color)

    elif start == "circle":
        radius = int(input("Enter radius: "))
        color = input("Enter a color: ")
        circle(pencil, radius, color)
    
    elif start == "pentagon":
        size = int(input("Enter a size: "))
        color = input("Enter a color: ")
        pentagon(pencil, size, color)
    else:
        print("Error: Shape not Found!")

    start = input("square/circle/pentagon: ").lower()
done()
