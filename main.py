import requests
from datetime import datetime
API_ID = "f339fe19"
API_KEY="eb1edde61d4605ccf5e8cd83eb56c569"
MY_WEIGHT = 56.6
MY_HEIGHT = 158.64
MY_AGE = 19

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_header = {
    "x-app-id":API_ID,
    "x-app-key":API_KEY,
}
query = input("Tell me which exercises you did: ")
exercise_params = {
    "query":query,
    "gender":"female",
     "weight_kg":MY_WEIGHT,
     "height_cm":MY_HEIGHT,
     "age":MY_AGE
}
response = requests.post(url=exercise_endpoint,json=exercise_params,headers=exercise_header)
resp = response.json()

###########################################
today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
sheety_endpoint = "https://api.sheety.co/10c8b4608cf98731e59f63baecb26874/myWorkout/sheet1"

for exercise in resp["exercises"]:
    sheet_params = {
        "sheet1":{
            "Date":today,
            "Time":time_now,
            "Exercise": exercise["name"].title(),
            "Duration": exercise["duration_min"],
            "Calories": exercise["nf_calories"]
        }
    }
    respon = requests.post(sheety_endpoint,json=sheet_params)
    print(respon.text)