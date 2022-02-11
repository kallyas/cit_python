# payements using africastalking

from __future__ import print_function
import africastalking

class Payements:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key
        self.africastalking = africastalking.initialize(self.username, self.api_key)
        self.payments = africastalking.Payment

    def b2c(self):
        productName = "bus_ticket"
        phoneNumber = "+256752541359"
        currencyCode = "UGX"
        amount = 1000
        provider_channel = "123466"

        metadata = {
            "transactionId": "1234",
            "message": "Payment for bus ticket"
        }

        try:
            res = self.payments.mobile_checkout(productName, phoneNumber, currencyCode, amount, provider_channel, metadata)
            print(res)
        except Exception as e:
            print(e)




if __name__ == '__main__':
    username = "sandbox"
    api_key = "API_KEY"
    payements = Payements(username, api_key)
    payements.b2c()
