import requests
from datetime import datetime, timedelta
from flight_data import FlightData
from pprint import pprint

"""https://tequila.kiwi.com/portal/docs/tequila_api/locations_api"""
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "q6fA8loTAUjQXLxLnJ0NJkOoCAvlHTj0"
headers = {
    "apikey": TEQUILA_API_KEY,
}
# cities = ["Paris","Berlin","Tokyo","Sydney","Istanbul","Kuala Lumpur","New York","San Francisco","Cape Town"]
from_date = (datetime.now() + timedelta(days=1))

to_date = (datetime.now() + timedelta(days=180))


# TODO 01 get_destimation_code assiging testing string and return that string
class FlightSearch:
    #  todo - 07  TO GET THE ACTUAL IATA CODE,  use get method in location based query
    #   return the code
    def get_destination_code(self, city_name):
        body = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city"
        }

        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=body, headers=headers)
        # print(response.status_code)
        data1 = response.json()
        code = data1['locations'][0]["code"]

        return code
# TODO -11 check flight using 3 parameters outside
#  use get() using search query in flight search api
    def check_flight(self, origin_city_code, destination_code, lowest_price_margin):
        # print(f"Check flights triggered for {destination_code}")
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "adults": 1,
            "curr": "GBP",
            "locale": "en",
            "price_from": lowest_price_margin,
            "one_for_city": 1,
            "max_stopovers": 0,
            "flight_type": "round",
        }
        response_flight = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=headers)
        # print(response_flight.status_code)
        data_res = response_flight.json()

        try:
            data = data_res['data'][0]
        except IndexError:
            query["max_stopovers"] =1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                departure_date=data['route'][0]['local_departure'].split("T")[0],
                arrival_date=data['route'][1]['local_departure'].split("T")[0],
                max_stepover=1,
                via_city=data["route"][0]["cityTo"]
            )
            # print(f"{flight_data.destination_city} : £{flight_data.price}")

            # pprint(data)
            print(flight_data.max_stepover)
            return flight_data
# TODO - 12 useFlightdata class to organise the flight details
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                departure_date=data['route'][0]['local_departure'].split("T")[0],
                arrival_date=data['route'][1]['local_departure'].split("T")[0],

            )
            # print(f"{flight_data.destination_city} : £{flight_data.price}")

            # pprint(data)
            return flight_data
