#19.12.2024
#laumets
#ülesanne 7
#7.1
# nimi = ["jüri pootsman", "mari jürgens", "ansambel maali", "juulikuus lumi maas"]
  
# # for i in nimi:
# #     print(i)
# # 
# for i in range(4):
#     print(f"{i+1}. {nimi[i]}")
    
# valik = int(input("Vali lugu (1-4): "))
# print(f"Mängin: {nimi[valik-1]}")



#7.2
jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
temps = []


print(f"Mõõdetav kuu: {jtemp[0]}")
print(f"Viimase mõõtmise tulemus: {jtemp[-1]} kraadi")


maks = 0
mini = 100
summa = 0
kokku = 0
kordused = 0


for t in range(1,len(jtemp)):
    print(jtemp[t], end=" ") #prindib kõik tempid
    if jtemp[t]>maks:        #max temp kontroll     
        maks = jtemp[t]
    if jtemp[t]<mini:        #min temp kontroll       
        mini = jtemp[t]
    summa+=jtemp[t]
    kokku+=1
    if jtemp[t]== -20:
        kordused+=1
       
temps.append(jtemp[t])

jtemp.pop(5)             #kustutab  
jtemp.insert(5,20)       #lisab
temps.sort()   


print()
print(f"Maksimum temp on: {maks}")
print(f"Miinimum temp on: {mini}")
print(f"Keskmine temp on: {summa/kokku:0.2f}")
print(f"Temp -20 esineb: {kordused} korda")
print(temps)


       