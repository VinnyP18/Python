import os
from flight_data import FlightData
from twilio.rest import Client
import smtplib

ACCOUNT_SSID = os.getenv('SSID')
AUTH_TOKEN = os.getenv('NOTETOKEN')
SMTP_SERVER = os.getenv('SMTP')
SMTP_USER = os.getenv('USER')
SMTP_PASSWORD = os.getenv('PASSWORD')

class NotificationManager(FlightData):

    def __init__(self, flights, is_direct, email):
        super().__init__(flights)
        self.flight = FlightData(flights)
        self.is_direct = is_direct
        self.email = email

        client = Client(ACCOUNT_SSID, AUTH_TOKEN)
        if self.is_direct:
            message = client.messages.create(
            body=f"Low price Alert! Only {self.flight.price} to fly from "
                 f"{self.flight.departure_code} to {self.flight.arrival_code} "
                 f"on {self.flight.departure_date} until {self.flight.arrival_date} direct.",
            from_="+18555289236",
            to="+18777804236",
            )
        else:
            message = client.messages.create(
                body=f"Low price Alert! Only {self.flight.price} to fly from "
                     f"{self.flight.departure_code} to {self.flight.arrival_code} "
                     f"on {self.flight.departure_date} until {self.flight.arrival_date} "
                     f"with {self.flight.stops} stop(s).",
                from_="+18555289236",
                to="+18777804236",
            )
        self.send_emails()


    def send_emails(self):

        with smtplib.SMTP(SMTP_SERVER, 587) as connection:
            connection.starttls()
            connection.login(user=SMTP_USER, password=SMTP_PASSWORD)
            if self.is_direct:
                msg = (f"Subject:Flight Club Deals!\n\nLow price Alert! Only {self.flight.price} "
                       f"to fly from {self.flight.departure_code} to {self.flight.arrival_code} on "
                       f"{self.flight.departure_date} until {self.flight.arrival_date} direct.")
            else:
                msg = (f"Subject:Flight Club Deals!\n\nLow price Alert! Only {self.flight.price} "
                       f"to fly from {self.flight.departure_code} to {self.flight.arrival_code} on "
                       f"{self.flight.departure_date} until {self.flight.arrival_date} "
                       f"with {self.flight.stops} stop(s).")

            connection.sendmail(
                from_addr=SMTP_USER,
                to_addrs=self.email,
                msg=msg.encode('utf-8')
            )