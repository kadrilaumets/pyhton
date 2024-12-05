# 02.ülesanne
# 05.12.2024 Kadri Laumets
import turtle
t = turtle.Turtle()

"""
 Loo aken, mille nimi on “Olümpiarõngad ja sinu nimi”
 Akna suurus 500×400
 Loo värvilised 50px olümpiarõngad (sinine, must, punane, kollane, roheline)
 Joone paksus 6
 Kiirus 0
 
"""
#akna loomine
aken = turtle.Screen()
aken.setup(width=500, height=400)
aken.title("Olümpiarõngad, Kadri")
#sinine
t.speed(0)
t.penup()
t.goto(-200,100)
t.pendown()
t.color("blue")
t.pensize(6)
t.circle(50,360)
#must
t.penup()
t.goto(-90,100)
t.pendown()
t.color("black")
t.pensize(6)
t.circle(50,360)
#punane
t.penup()
t.goto(20,100)
t.pendown()
t.color("red")
t.pensize(6)
t.circle(50,360)
#kollane
t.penup()
t.goto(-150,50)
t.pendown()
t.color("yellow")
t.pensize(6)
t.circle(50,360)
#roheline
t.penup()
t.goto(-30,50)
t.pendown()
t.color("green")
t.pensize(6)
t.circle(50,360)


turtle.done()