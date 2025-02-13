#13.02
#kadri laumets
#ülesanne 16

import os
from datetime import date
print (f"Tere {os.getlogin()}")
print (f"Sinu rada {os.getcwd()}")

kataloogidearv = 10
kustuta = 5
kp = str(date.today())

try:
    os.mkdir(kp)
    print(f"{kp} kaust on loodud")
    for i in range(1,kataloogidearv+1):
        kaust = kp+"/"+ str(i)
        os.makedirs(kaust)
except:
    print("Kataloog on juba olemas")

if os.path.exists(kp+"/"+str(kustuta)):
    os.rmdir(kp+"/"+str(kustuta))
    print(f"{kustuta} kataloog kustutatud")
else:
    print(f"{kustuta} kataloogi ei leitud")