#M5T1b - initials
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

    #draw a R
    t.penup()
    t.back(300)
    t.pendown()
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(400)
    t.left(90)

    t.penup()
    t.forward(200)
    t.pendown()
    t.left(135)
    t.forward(280)

    #draw a C
    t.penup()
    t.right(135)
    t.forward(600)
    t.pendown()

    t.penup()
    t.left(90)
    t.forward(200)
    t.pendown()
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
        
main()
