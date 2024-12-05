# 01.ülesanne
# Kadri 05.12.2024
import turtle
#kolmnurk
turtle.speed(6) #reguleeri 1-9
turtle.penup()
turtle.goto(-500,200) #liigutab asukohta
turtle.pendown()
turtle.forward(200)# liigub edasi,pikslites
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)

# süda

turtle.penup()
turtle.goto(-200,200) # liigutab asukohta
turtle.pendown()
turtle.forward(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.fd(100)

# lõpetab, ennetab kokku jooksmise
turtle.done()