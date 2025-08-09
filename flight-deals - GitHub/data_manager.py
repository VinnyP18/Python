import requests
import os

SHEETLY_TOKEN = os.getenv('TOKEN')

SHEETLY_URL_PRICES_PULL = f'{os.getenv('FLIGHTSHEET')}/prices'
SHEETLY_URL_PRICE_PUT = f'{os.getenv('FLIGHTSHEET')}/prices/'

SHEETLY_URL_USERS_PULL = f'{os.getenv('FLIGHTSHEET')}/users'
SHEETLY_URL_USERS_PUT = f'{os.getenv('FLIGHTSHEET')}/users/'

SHEETLY_HEADER = {
    'Authorization' : "Bearer %dWPEIA2dGWuNwufI1d$LUZ!vis3Be0XdtB@6IwxEkeHk4CEpkjuzVRqCEt3Bq3H"
}
class DataManager:

    def __init__(self):

        self.info = self.pull_info()
        self.user_emails = self.get_customer_emails()

    def pull_info(self):
        response = requests.get(url=SHEETLY_URL_PRICES_PULL,
                                headers=SHEETLY_HEADER)
        return response.json()

    def put_info(self, city_code, row_id):
        put_values = {
            'price' : {
                'iataCode' : city_code,
            }
        }
        requests.put(url=f'{SHEETLY_URL_PRICE_PUT}{row_id}',
                                headers=SHEETLY_HEADER,
                                json=put_values)

    def get_customer_emails(self):
        response = requests.get(url=SHEETLY_URL_USERS_PULL,
                                headers=SHEETLY_HEADER)

        # dict = {'users': [{'timestamp': '6/17/2025 18:45:22', 'whatIsYourFirstName?': 'Udemy', 'whatIsYourLastName?': 'Test', 'whatIsYourEmail?': 'udemytest79@gmail.com', 'id': 2}, {'timestamp': '6/17/2025 18:48:44', 'whatIsYourFirstName?': 'Udemy', 'whatIsYourLastName?': 'Test2', 'whatIsYourEmail?': 'udemytest79@outlook.com', 'id': 3}]}
        return [value['whatIsYourEmail?'] for value in response.json()['users']]

# {'users': [{'timestamp': '6/17/2025 18:45:22', 'whatIsYourFirstName?': 'Udemy', 'whatIsYourLastName?': 'Test', 'whatIsYourEmail?': 'udemytest79@gmail.com', 'id': 2}, {'timestamp': '6/17/2025 18:48:44', 'whatIsYourFirstName?': 'Udemy', 'whatIsYourLastName?': 'Test2', 'whatIsYourEmail?': 'udemytest79@outlook.com', 'id': 3}]}
