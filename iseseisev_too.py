import json
import requests
import statistics


url = "https://www.metshein.com/kordamine/json/autod.json"
response = requests.get(url)
data=response.json()
#print(data)


#kõige odavam ja kõige kallim
odav_hind = min(hind["hind"] for hind in data["autod"])
print(f"Kõige odavam hind on {odav_hind}.")

kallim_hind = max(hind["hind"] for hind in data["autod"])
print(f"Kõige kallim hind on {kallim_hind}.")


# #bmw keskmine hind
bmw_hinnad=[]
for auto in data["autod"]:
    if auto["mark"]=="BMW":
        bmw_hinnad.append(auto["hind"])
        #print(bmw_hinnad)

keskmine = statistics.mean(bmw_hinnad)
print(f"Keskmine BMW hind on {keskmine:0.2f}.")

# #kõik autod alla 10000
autod=[]
for auto in data["autod"]:
    if auto["hind"]<10000:
        autod.append(auto["mark"]+" "+auto["mudel"])

print(f"Autod, mille hind jääb alla 10000 on: {autod}")



