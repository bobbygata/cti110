#M5lab - snowflakes
#CTI 110
#Robert Crawford
#10/16/2017

def main():
    import turtle
    win = turtle.Screen()
    t = turtle.Turtle()
    win.bgcolor("blue")
    
    # display options
    t.pensize(6)
    t.pencolor('white')
    t.shape("turtle")
    t.speed(10)

    for i in range(36):
        for i in range(2):
            t.forward(100)
            t.right(60)
            t.forward(100)
            t.right(120)
        t.right(10)

main()


    
