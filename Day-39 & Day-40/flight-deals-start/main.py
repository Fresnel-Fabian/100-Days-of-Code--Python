# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.read()
pprint(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update()

for destination in sheet_data:
    flight = flight_search.search(destination["iataCode"])
    if flight == "None":
        continue

    if flight.price <= destination["lowestPrice"]:
        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["first"] for row in users]
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city} - {flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        print(message)
        notification_manager.send_email(emails, message)
        # notification_manager.send_sms(
        #     message=f"Low price alert! Only ${flight.price} ot fly from{flight.origin_city}-{flight.origin_airport}"
        #             f" to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to "
        #             f"{flight.return_date}."
        # )
