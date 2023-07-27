import requests
from datetime import datetime

MY_LAT = 8.524139
MY_LONG = 76.936638

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
# print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# print(longitude)
# print(latitude)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response_1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_1.raise_for_status()
data_1 = response_1.json()
sunrise = data_1["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_1["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now = datetime.now()
print(time_now.hour)
