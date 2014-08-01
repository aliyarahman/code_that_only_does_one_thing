# Import the tools we need - they are in the requirements.txt file
from twilio.rest import TwilioRestClient 
 
# Enter your credentials 
ACCOUNT_SID = "[hidden on Github]" 
AUTH_TOKEN = "[hidden on Github]" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) # Connect and authenticate
 
client.messages.create(
	to="+15135551234",		# This is who we're sending it to 
	from_="+18702294975", 		# This is our Twilio number
	body="What's good?",  		# This is the message content
)
