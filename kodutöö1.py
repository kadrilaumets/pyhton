#Kadri Laumets
#iseseisev ülesanne 01

import turtle

ruudukylg =  200
kolmnurk = 200
uks_kylg = 100
turtle.speed(5)
turtle.pensize(5)

for _ in range(4):
    turtle.forward(ruudukylg)
    turtle.left(90)

turtle.penup()
turtle.goto(0,ruudukylg)
turtle.pendown()

for _ in range (3):
    turtle.pencolor("green")
    turtle.forward(kolmnurk)
    turtle.left(120)

turtle.penup()
turtle.goto(ruudukylg/4,0)
turtle.pendown()

for _ in range(4):
    turtle.pencolor("red")
    turtle.forward(uks_kylg)
    turtle.left(90)

turtle.penup()
turtle.goto(ruudukylg,0)
turtle.pendown()

for _ in range(4):
    turtle.left(90)
    turtle.color("black")
    turtle.forward(ruudukylg)
    

turtle.penup()
turtle.goto(0,ruudukylg)
turtle.pendown()


turtle.done()
