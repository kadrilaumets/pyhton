#30.01
#Kadri Laumets

#2.1
aratus = input("Mitu korda kell heliseb?")
for i in range(int(aratus)):
    print("Tõuse ja sära!")

#2.2
ringide_arv = int(input("Sisesta ringide arv: "))

summa = 0
ring = 2

while ring <= ringide_arv:
    summa += ring
    ring += 2

print("Saadud porgandite koguarv:", summa)

#2.3
import random

taringute_arv = int(input("Sisesta täringute arv: "))
for i in range(taringute_arv):
    vise = random.randint(1,6)
    print(vise)

#2.4
ruut = int(input("Sisesta ruudu järjekorranumber (1-64): "))

nisuterade_arv = 1
loendur = 1

while loendur < ruut:
    nisuterade_arv *= 2
    loendur += 1

print(f"Ruudul {ruut} on tasuks {nisuterade_arv} nisutera.")

#2.5
import random

ounad = 14
poialpoisid = int(input("Mitu pöialpoissi tahab õunu? (0-7): "))

for i in range(poialpoisid):
    antud_ounad = random.randint(1,2)
    print(f"Pöialpoiss {i+1} sai {antud_ounad} õuna.")
    ounad -= antud_ounad


print(f"Lumivalgekesele jäi {ounad} õuna.")
