#It will write alphabets
import turtle

def draw_name():
    window = turtle.Screen()
    window.bgcolor("pink")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("white")
    brad.speed(100)

    #brad.write("Anshu Sobti")
    # It will write K
    brad.left(90)
    brad.forward(100)
    brad.backward(50)
    brad.right(45)
    brad.forward(65)
    brad.backward(65)
    brad.right(90)
    brad.forward(65)

    #It will write S
    x = brad.pos()
    #print(x)
    brad.pu()
    brad.setpos(65,4.04)
    brad.pd()
    brad.left(45)
    brad.forward(50)
    brad.left(90)
    brad.forward(50)
    brad.left(90)
    brad.forward(50)
    brad.right(90)
    brad.forward(50)
    brad.right(90)
    brad.forward(50)

    #It will write A
    x = brad.pos()
    #print(x)
    brad.pu()
    brad.setpos(135,4.04)
    brad.pd()
    brad.left(60)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    brad.backward(50)
    brad.right(120)
    brad.forward(50)
    
    windows.exitonclick()

draw_name()
