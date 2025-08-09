from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

#===================================================================================
# CONSTANTS
#===================================================================================

ORIGIN = 'LON'

#===================================================================================
# MAIN
#===================================================================================

"""

The following 'destinations' dictionary is used when testing so continuous API calls 
 are not needed and call limits are not reached.

"""

# destinations = [
#     {
#         'city': 'Paris',
#         'iataCode': 'PAR',
#         'lowestPrice': 54,
#         'id': 2
#     },
#     {
#         'city': 'Frankfurt',
#         'iataCode': 'FRA',
#         'lowestPrice': 42, 'id': 3
#     },
#     {
#         'city': 'Tokyo',
#         'iataCode': 'TYO',
#         'lowestPrice': 900,
#         'id': 4
#     },
#     {
#         'city': 'Hong Kong',
#         'iataCode': 'HKG',
#         'lowestPrice': 551,
#         'id': 5
#     },
#     {
#         'city': 'Istanbul',
#         'iataCode': 'IST',
#         'lowestPrice': 95,
#         'id': 6
#     },
#     {
#         'city': 'Kuala Lumpur',
#         'iataCode': 'KUL',
#         'lowestPrice': 414,
#         'id': 7
#     },
#     {
#         'city': 'New York',
#         'iataCode': 'NYC',
#         'lowestPrice': 240,
#         'id': 8
#     },
#     {
#         'city': 'San Francisco',
#         'iataCode': 'SFO',
#         'lowestPrice': 260,
#         'id': 9
#     },
#     {
#         'city': 'Dublin',
#         'iataCode': 'DBN',
#         'lowestPrice': 378,
#         'id': 10
#     }
# ]

info = DataManager()
destinations = info.info['prices']
user_emails = info.user_emails
search = FlightSearch()

for destination in destinations:
    if destination['iataCode'] == '':
        city_code = search.get_city_code(destination['city'])
        info.put_info(city_code,destination['id'])
    flights = search.get_flights(ORIGIN ,destination['iataCode'], destination['lowestPrice'])
    if flights:
        for flight in flights:
            if int(flight['id']) % 2 != 0:
                for email in user_emails:
                    notification_manager = NotificationManager(flight, search.is_direct, email)
