import requests

api = "https://api.sheety.co/7a3b35df91c229538802826f12ce0f39/flightDeals/users"
print("Welcome to Fresnel's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is your email?")
email_confirm = input("Type your email again.")
if email == email_confirm:
    print("You're in the club!")
    data = {
        "user": {
            "first": first_name,
            "last": last_name,
            "email": email,
        }
    }
    response = requests.post(url=api, json=data)
    print(response.raise_for_status)
