#harjutus 8
#laumets
#17.01.2025

#8.1
telefonid={
'Mari': '5957503',
'Toomas': '5719979',
'Kertu': '5201750',
'Siim': '5580027',
'Piret': '5960799',
'Jaan': '5160415',
'Lea': '5760164',
'Mart': '5337951',
'Anni': '5004818',
'Tõnu': '5721873',
'Kai': '5811884',
'Rasmus': '5859489',
'Eva': '5039393',
'Oskar': '5635812',
'Liina': '5696114',
'Peeter': '5560756',
'Sandra': '5257415',
'Heiki': '5207248',
'Kristi': '5703338',
'Urmas': '5400549'
}
print(f"Rasmuse telefoninumber on {telefonid['Rasmus']}")
telefonid.pop("Kristi")
telefonid["Eva"]=5555555
print(telefonid)
print()

for nimi in telefonid:
    print(telefonid[nimi], end=" ")
print()
try:
    otsi = input("otsi: ")
    print(f"Leitud: {telefonid[otsi]}")
except:
    print("Otsitavat ei leitud")


#8.2
tooted = {
'piim': {'kogus': 20, 'hind': 1.19},
'küpsised': {'kogus': 20, 'hind': 4.99},
'või': {'kogus': 20, 'hind': 2.29},
'juust': {'kogus': 15, 'hind': 1.9},
'leib': {'kogus': 15, 'hind': 2.59},
'jogurt': {'kogus': 18, 'hind': 3.65},
'õunad': {'kogus': 35, 'hind': 3.15},
'apelsinid': {'kogus': 40, 'hind': 0.99},
'banaanid': {'kogus': 23, 'hind': 1.29}
}
try:
    toode = input("Vali toode: ")
    if toode in tooted:
        kogus = int(input("Lisa kogus: "))
        if kogus<=tooted[toode]["kogus"]:
            hind = tooted[toode]["hind"]
            summa = round(hind * kogus,2)
            print(summa)
            tooted[toode]["kogus"]-=kogus
            print(f"Laoseis: {tooted[toode]["kogus"]}")
        else:
            print("Sellist kogust pole")
    else:
        print("Sellist toodet pole")
except:
    print("Midagi on valesti!")

