#M5T1a - shapes
#CTI 110
#Robert Crawford
#10/11/2017

def main():
    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()

    # display options
    t.pensize(6)
    t.pencolor("lime green")
    t.shape("turtle")
    t.speed(5)

    # square with no loop
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)

    # triangle with no loop 
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)
    t.forward(50)
    t.left(120)

    # squre with loop
    for i in range (4):
        t.forward(100)
        t.left(90)

    # triangle with loop 
    for i in range (3):
        t.forward(100)
        t.left(120)


main()
