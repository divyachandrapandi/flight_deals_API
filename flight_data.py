class FlightData:

    def __init__(self, origin_city, origin_airport, price, destination_city, destination_airport,
                 departure_date, arrival_date, max_stepover=0, via_city=""):
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.price = price
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.max_stepover = max_stepover
        self.via_city = via_city
