# 03.ülesanne
# 05.12.2024 Kadri Laumets
import turtle
#3.1
nimi = "Karin" #sõne,string, str
vanus = 20 #int, integer, täisarv
keskmine_hinne = 4.53 # komaarv, float, punktiga
#teisendamine tekstiks
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))
#loetelu komadega
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne) 
#lause vormindamine muutujatega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinna on {keskmine_hinne}")

#3.7
#andmed
kylje_pikkus = 300
nurk = 120
varv = "red"
#kolmnurk
turtle.speed(6) #reguleeri 1-9
turtle.color(varv)
turtle.forward(kylje_pikkus)# liigub edasi,pikslites
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
#asukoha muutmine
turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()
#järgmine kolmnurk
turtle.color(varv)
turtle.forward(kylje_pikkus)# liigub edasi,pikslites
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
#asukoha muutmine
turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()
# kolmas kolmnurk
turtle.color(varv)
turtle.forward(kylje_pikkus)# liigub edasi,pikslites
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)

turtle.done()

