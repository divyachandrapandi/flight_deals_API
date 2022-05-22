
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
# TODO 4. Pass the data back to the main.py file, so that you can print the data from main.py
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)
ORIGIN_CITY_CODE = "LON"
# TODO 5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.


if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")
    # TODO - 08  updating sheet data with data_manager.update
    data_manager.destination_data = sheet_data

    data_manager.update_destination_codes()
# TODO -10, sheetdata updated
# print(sheet_data)
# TODO -13 for each city in sheet_Data we gonna get flight details
for destination in sheet_data:
    check_flight = flight_search.check_flight(
        ORIGIN_CITY_CODE,
        destination['iataCode'],
        destination["lowestPrice"]
    )
# TODO - 14 we got seven parameter for notification_manager from check_flight
#     if check_flight details are not none and price must cheaper
    if check_flight is not None and int(destination['lowestPrice']) < int(check_flight.price):
        notification = NotificationManager(price=int(check_flight.price), origin_city=check_flight.origin_city,
                                           origin_airport=check_flight.origin_airport,
                                           dest_city=check_flight.destination_city,
                                           dest_airport=check_flight.destination_airport,
                                           d_date=check_flight.departure_date,
                                           a_date=check_flight.arrival_date,
                                           stopover =check_flight.max_stepover,
                                           via_city=check_flight.via_city)

