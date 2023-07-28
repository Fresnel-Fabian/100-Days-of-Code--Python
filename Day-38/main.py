import datetime
import requests
import os

# SHEET_USERNAME = os.environ["SHEET_USERNAME"]
SHEET_USERNAME = os.environ.get("SHEET_USERNAME")
# SHEET_USERNAME = "Fresnel_Fabian"
SHEET_PASSWORD = "Family@123"
NUTRITIONX_APP_ID = "dc1db1b2"
NUTRITIONX_APP_KEY = "3717db00e7e5986a766956df4087963a"
NUTRITIONX_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/7a3b35df91c229538802826f12ce0f39/myWorkouts/workouts"

headers = {
    "x-app-id": NUTRITIONX_APP_ID,
    "x-app-key": NUTRITIONX_APP_KEY,
}
query = input("Exercise done today: ")
parameters = {
    "query": query,
    "gender": "MALE",
    "weight_kg": 75.5,
    "height_cm": 177.5,
    "age": 21,
}
response = requests.post(url=NUTRITIONX_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)
print(result["exercises"][0]["user_input"])
date = datetime.datetime.now()
print(date.strftime("%d/%m/%Y"))
print(date.strftime("%H:%M:%S"))
for exercise in result["exercises"]:
    exercise_date = {
        "workout": {
            "date": date.strftime("%d/%m/%Y"),
            "time": date.strftime("%H:%M:%S"),
            "exercise": (exercise["user_input"]).title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    headers = {"Authorization": "Bearer hofhdldffjldfodofhod"}
    print(exercise_date)
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=exercise_date, headers=headers)
    print(sheet_response.status_code)