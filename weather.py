import requests

city=input("Enter Your City --> ")
Api_Key = "a730448f523416f46aa7cfc0c1d72643" # Paste Your API ID Here

final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)

result = requests.get(final_URL)
data = result.json()

temprature = data['main']['temp']
cordinatelon = data['coord']['lon']
cordinatelat = data['coord']['lat']

print(temprature," ",cordinatelat," ",cordinatelon)
