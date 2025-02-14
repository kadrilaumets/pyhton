import requests

# API võtme ja linna nime määramine
city = "Haapsalu"
api_key = "dbdfccc992b6b3165b638303055574ce"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)