import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")
    angiel = turtle.Turtle()
    angiel.shape("turtle") #shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”
    angiel.color("white")
    angiel.speed(100)
    angiel.pu()
    angiel.setpos(0,-200)
    angiel.pd()
    angiel.left(90)
    angiel.forward(200)

    angiel.left(60)
    j=1
    x=15
    y=360/x
    while j<y+1:
        i=1
        while i<4:
            angiel.forward(100)
            angiel.left(120)
            i=i+1
        angiel.left(x)
        j=j+1
        
    window.exitonclick()

draw_flower()
