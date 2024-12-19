# 19.12.2024
# ülesanne 5
"""
Ilmaennustuse rakendus (and)
Sinu ülesanne on luua lihtne Pythoni programm, mis aitab kasutajal valida sobiva riietuse vastavalt ilmale.
Kasutaja sisestab temperatuuri (Celsius). Kui temperatuur on alla 0 kraadi, peab programm väljastama soovituse kanda talveriideid. Kui temperatuur on vahemikus 0 kuni 15 kraadi, peaks programm soovitama kanda kevad-sügis rõivaid. Kui temperatuur on üle 15 kraadi, soovitab programm kanda suveriideid.
Kasuta if, elif ja else lauseid selle ülesande lahendamiseks.
"""
# try:
#     kraadid = 10
#     
#     if kraadid < 0:
#         print("Talveriided")
#     elif kraadid >= 0 or kraadid <= 15:
#         print("Kevad-sügis")
#     else:
#         print("Suvi")
# except:
#     print("Viga sisestuses!")
#     
"""
Matemaatika test (randint)
Kirjuta programm, mis kontrollib kasutaja poolt sisestatud vastust lihtsale matemaatikaülesandele.
Näiteks, programm esitab küsimuse “Mis on 3 korda 4?”. Kasutaja peab sisestama vastuse. Kui kasutaja vastus on 12, siis programm väljastab “Õige vastus!”, kui aga vastus on midagi muud, siis väljastab “Vale vastus, proovi uuesti!”.
Kasuta if ja else lauseid selleks, et kontrollida kasutaja sisestatud vastust.
"""
import random

try:
    arv1 = random.randint(1,10)
    arv2 = random.randint(1,10)
    vastus = int(input(f"{arv1}*{arv2}="))
    
except:
    print("Viga sisestuses!")













"""
Mündiviskamise äraarvamine koos juhuslikkusega (and ja or)
Kirjuta programm, mis simuleerib mündiviskamist. Programm genereerib juhusliku tulemuse – “kiri” või “kull”, kasutades random.randint(0,1) funktsiooni. Programmi koostamisel pead importima import random mooduli ja kasutama randint() funktsiooni, et valida kahe võimaliku tulemuse vahel. Näiteks, kui randint(0, 1) annab tulemuseks 0, siis võib see tähendada “kirja”, ja 1 võib tähendada “kulli”.
Seejärel palub programm kasutajal arvata, kumb külg maandub ülespoole.
Kasuta if lauset, et kontrollida, kas kasutaja arvas õigesti. Kui arvas õigesti, siis joonista Turtle abil roheline ring; kui valesti, siis punane ring.
"""