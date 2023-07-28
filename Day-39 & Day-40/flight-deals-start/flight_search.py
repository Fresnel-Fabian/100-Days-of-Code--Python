from pprint import pprint

import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "cWWVvv611-xHlHQfEKtPa0dN9s1oTWpk"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def destination_code(self, city_name):
        # Return "Testing" for now to make sure sheety is working
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search(self, destination_iatacode):
        datefrom = datetime.now()
        dateto = datefrom + timedelta(days=182.625)
        query = {
            "fly_from": "LON",
            "fly_to": destination_iatacode,
            "dateFrom": datefrom.strftime("%d/%m/%Y"),
            "dateTo": dateto.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
        print(response.json())
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"Not flights found for {destination_iatacode}")
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_over=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:

            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=0,
                via_city="",
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data

