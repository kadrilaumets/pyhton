
def konto_haldur(algne_saldo, toiming, summa):
    if toiming == 'deposiit':
        algne_saldo += summa
    elif toiming == 'valjavote':
        if summa > algne_saldo:
            return "Kontol ple piisavalt raha."
        algne_saldo -= summa
    else:
        print("Viga")
    
    return algne_saldo

saldo = 100

while True:
    print("\nPraegune konto saldo:", saldo)
    toiming = input("Kas soovite teha deposiiti või väljavõtet? (sisestage 'd' deposiidiks või 'v' väljavõtuks): ")
    
    if toiming == 'd':
        summa = float(input("Sisestage summa, mida soovite deposiitida: "))
        saldo = konto_haldur(saldo, 'deposiit', summa)
    elif toiming == 'v':
        summa = float(input("Sisestage summa, mida soovite välja võtta: "))
        saldo = konto_haldur(saldo, 'valjavote', summa)
    else:
        print("ära lollita")
        continue
    
    print("Uus saldo:", saldo)
    