#30.01
#Kadri Laumets

#3.1
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()

while True:
    aasta = int(input("Palun sisestage, millise aasta andmeid vajate (2011-2019): "))
    if 2011 <= aasta <= 2019:
        break
    else:
        print("Palun sisestage aasta vahemikus 2011 kuni 2019.")

index = aasta - 2011


print(f"{aasta}. aastal oli vastuvõetuid {vastuvõetud[index]}")

#3.2

def arvuta_porgandid(ringide_arv):
    kogu_porgandid = 0
    for i in range(2, ringide_arv + 1, 2):
        kogu_porgandid += i
    return kogu_porgandid

# Ask the user for the number of laps
ringide_arv = int(input("Sisestage ringide arv: "))

# Calculate the total number of carrots
kogu_porgandid = arvuta_porgandid(ringide_arv)

# Output the total number of carrots
print(f"Saadavate porgandite koguarv on {kogu_porgandid}.")

#3.3

with open("konto.txt", encoding="UTF-8") as fail:
    tehingud = fail.readlines()

# Print kõik pos summad
for tehing in tehingud:
    summa = float(tehing.strip())
    if summa > 0:
        print(summa)

#3.4


failinimi = input("Sisestage failinimi (koos laiendiga, nt jukebox.txt): ")

with open(failinimi, encoding="UTF-8") as fail:
    laulud = fail.readlines()
#näita laulud numbritega
for i, laul in enumerate(laulud, start=1):
    print(f"{i}. {laul.strip()}")

#küsi laulu numbrit
laulu_number = int(input("Mitmendat laulu soovite? "))

# näita valitud laulu
if 1 <= laulu_number <= len(laulud):
    print(f"Valitud laul: {laulud[laulu_number - 1].strip()}")
else:
    print("Vigane laulu number.")


#3.5

from datetime import datetime

#küsi failinime
failinimi = "nimekiri.txt"

with open(failinimi, encoding="UTF-8") as fail:
    nimed = fail.readlines()

# tänane kuupäev
tana_paev = datetime.now().day

# näita nime kes peaks täna vastama
if 1 <= tana_paev <= len(nimed):
    print(f"Täna peab vastama: {nimed[tana_paev - 1].strip()}")
else:
    print("Vigane kuupäev või nimekiri ei sisalda piisavalt nimesid.")

