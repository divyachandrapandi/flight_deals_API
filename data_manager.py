import requests

SHEETY_ENDPOINT = "https://api.sheety.co/159c57a4845f54585761b941dcef8bd7/flightDeals/prices"
SHEETY_API_BEARER = "Basic ZGl2eWE1NTpwYXNzaGF0ag=="
headers = {
    "Authorization": SHEETY_API_BEARER,
        }

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # TODO 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        data = response.json()
        # self.destination_data = data["prices"]
        # TODO 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        print(data)
        return self.destination_data

    # TODO 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    #  to update the Google Sheet with the IATA codes. (Do this using code).

    # TODO -09 for put request, use id for row assignement
    #  simple, get data from get() and use in update() to put data in sheet data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)
dataman = DataManager()
dataman.get_destination_data()