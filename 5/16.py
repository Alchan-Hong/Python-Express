import turtle

t = turtle.Turtle()
t.shape("turtle")


def draw_line():
    
    for i in range(1, 13):
        t.fd(100)
        t.backward(100)
        t.left(30)

draw_line()

turtle.mainloop()
turtle.bye()

