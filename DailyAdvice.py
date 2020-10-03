import requests
from twilio.rest import Client

account_sid = 'twilio_account_sid_here'
auth_token = 'twilio_token_here'
client = Client(account_sid, auth_token)


response = requests.get('https://api.adviceslip.com/advice')
adviceResponse = response.json()
advice = adviceResponse['slip']['advice']


message = client.messages.create(
                               from_='whatsapp:from_number_here',
                              body=advice,
                              to='whatsapp:to_number_here'
                          )
print(message.sid)
