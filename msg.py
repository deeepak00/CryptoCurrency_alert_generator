from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

message = client.messages.create(body="Hi",from_=keys.twilio_account, to=keys.my_number)
