import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7a3b35df91c229538802826f12ce0f39/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/7a3b35df91c229538802826f12ce0f39/flightDeals/users"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def read(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # def write(self):
    #     response = requests.po
    def update(self):
        for city in self.destination_data:
            new_data = {
                "price"
                "": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response)
    def get_customer_emails(self):
        customer_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customer_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data