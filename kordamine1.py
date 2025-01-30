#30.01
#Kadri Laumets

#1.1
print("Tere, maailm!")

# #1.2
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = " aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

# #1.3
korgus = float(input("Kui mitme km kõrgusel on pilv?"))
if korgus > 6.0:
    print("Need on ülemised pilved")
else:
    print("Need ei ole ülemised pilved")

#1.4
inimeste_arv = int(input("sisesta inimeste arv: "))
kohtade_arv = int(input("Sisesta ühe bussi kohtade arv: "))

#täis busside arv
busse_vaja = inimeste_arv // kohtade_arv
#ülejaak
ulejaak = inimeste_arv % kohtade_arv

#kui ülejääk on vaja extra bussi
if ulejaak > 0:
    busse_vaja += 1
    viimases_bussis = ulejaak
else:
    viimases_bussis = kohtade_arv #viimane buss on täis, kui pole ülejääki

print("\nInimeste arv:", inimeste_arv)
print("Kohtade arv:", kohtade_arv)
print("Busse vaja:", busse_vaja)
print("Viimases bussis inimesi:", viimases_bussis)




