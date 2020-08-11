# Import the tools we need - they are in the requirements.txt file
from twilio.rest import TwilioRestClient 
 
# Enter your credentials 
ACCOUNT_SID = "AC6508fae9294cd6c44e75ae8dc5e3fea4" 
AUTH_TOKEN = "0b59c3e3bea8bc7293b5cd8ba4a3ac34"


client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) # Connect and authenticate
 
client.messages.create(
	to="+17277100829",		# This is who we're sending it to 
	from_="+18592794269", 		# This is our Twilio number
	body="Hey girl, you use the internet?",  		# This is the message content
)
