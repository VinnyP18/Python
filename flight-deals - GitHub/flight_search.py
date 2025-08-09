from datetime import datetime, timedelta
import requests
import os

AMADEUS_URL_BASE_V1 = 'https://test.api.amadeus.com/v1'
AMADEUS_URL_BASE_V2 = 'https://test.api.amadeus.com/v2'
AMADEUS_CITY_URL = '/reference-data/locations/cities'

AMADEUS_FLIGHTS_URL = '/shopping/flight-offers'

AMADEUS_AUTHORIZATION_URL = 'https://test.api.amadeus.com/v1/security/oauth2/token'
AMADEUS_AUTHORIZATION_HEADER = {"Content-Type": 'application/x-www-form-urlencoded'}
AMADEUS_CLIENT = os.getenv('CLIENT')
AMADEUS_SECRET = os.getenv('SECRET')
AMADEUS_AUTHORIZATION_BODY = {
    "grant_type": "client_credentials",
    "client_id": AMADEUS_CLIENT,
    "client_secret": AMADEUS_SECRET,
}

ADULTS = 1

class FlightSearch:

    def __init__(self):
        self.departure = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        self.return_date = (datetime.now() + timedelta(days=(6 * 30))).strftime('%Y-%m-%d')
        self.is_direct = True

    def get_city_code(self, city):
        token = self.get_token()
        params = {
            'keyword' : f'{city.upper()}',
        }
        header = {"Authorization" : f"Bearer {token}"}
        response = requests.get(url=f'{AMADEUS_URL_BASE_V1}{AMADEUS_CITY_URL}',
                                headers=header,
                                params=params)

        return response.json()['data'][0]['iataCode']

    def get_token(self):
        response = requests.post(url=AMADEUS_AUTHORIZATION_URL,
                                 headers=AMADEUS_AUTHORIZATION_HEADER,
                                 data=AMADEUS_AUTHORIZATION_BODY)

        return response.json()['access_token']

    def get_flights(self, origin_city_code, city_code, price):
        token = self.get_token()
        params = {
            'originLocationCode' : origin_city_code,
            'destinationLocationCode' : city_code,
            'departureDate' : self.departure,
            'returnDate' : self.return_date,
            'adults' : ADULTS,
            'maxPrice' : price,
            'nonStop' : 'true'
        }
        header = {"Authorization": f"Bearer {token}"}
        response = requests.get(url=f'{AMADEUS_URL_BASE_V2}{AMADEUS_FLIGHTS_URL}',
                                headers=header,
                                params=params)

        if response.json()['data'] == []:
            params = {
                'originLocationCode': origin_city_code,
                'destinationLocationCode': city_code,
                'departureDate': self.departure,
                'returnDate': self.return_date,
                'adults': ADULTS,
                'maxPrice': price,
            }
            header = {"Authorization": f"Bearer {token}"}
            response = requests.get(url=f'{AMADEUS_URL_BASE_V2}{AMADEUS_FLIGHTS_URL}',
                                    headers=header,
                                    params=params)
            self.is_direct = False

        return response.json()['data']