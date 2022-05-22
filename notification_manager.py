from twilio.rest import Client

account_sid = SID"
auth_token = "TOKEN"
# TODO -14 to send sms, we need 7 parameters

class NotificationManager:
    def __init__(self, price, origin_city, origin_airport, dest_city, dest_airport, d_date, a_date, stopover, via_city):
        self.client = Client(account_sid, auth_token)
        self.query = f"Low Price Alert!!!Only £{price} to fly from {origin_city}-"
        f"{origin_airport} to {dest_city}-{dest_airport},"
        f"from {d_date} to {a_date}"

        message = self.client.messages \
            .create(
                body= self.query,
                from_=FROM,
                to=TO
                        )
        if stopover > 0:
            self.query += f"\nFlight has {stopover} stop over, via {via_city}."
            message = self.client.messages \
                .create(
                body=self.query,
                from_=FROM,
                to=TO
            )


        print(message.status)
