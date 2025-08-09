class FlightData:

    def __init__(self, flights):
        self.flights = flights
        self.departure_code = flights['itineraries'][0]['segments'][0]['departure']['iataCode']
        self.departure_date = flights['itineraries'][0]['segments'][0]['departure']['at'].split('T')[0]
        self.arrival_code = self.get_arrival_code()
        self.arrival_date = self.get_arrival_time()
        self.price = f"£{flights['price']['total']}"
        self.stops = len(flights['itineraries']) - 1

    def get_arrival_code(self):
        for flight in self.flights['itineraries'][0]['segments']:
            destination = flight['arrival']['iataCode']
        return destination

    def get_arrival_time(self):
        for flight in self.flights['itineraries']:
            arrival = flight['segments'][0]['arrival']['at'].split('T')[0]
        return arrival
