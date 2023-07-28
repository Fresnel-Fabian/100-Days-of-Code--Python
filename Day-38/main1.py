import requests

GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5" #entered random height in cm
AGE = "50"

APP_ID = "dc1db1b2"
API_KEY = "3717db00e7e5986a766956df4087963a"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)