#!usr/bin/env python

import twitter  # This uses the python-twitter package. Install that using pip before you start.

# Section 1: Establish your credentials with the Twitter API"
consumer_key = "enter_your_own_here"
consumer_secret = "enter_your_own_here"
access_token = "enter_your_own_here"
access_secret = "enter_your_own_here"


# Section 1.2: Open a secure connection to Twitter's API
api = twitter.Api(consumer_key = consumer_key,consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_secret)



# Section 2: Ask your question and store the answer
search = api.GetSearch(term='alternativefacts', lang='en',result_type='recent')

# Section 3: Awesome, I have info - now I want to do stuff to it on my own machine
for s in search:
	print s.user.screen_name + "says: \t" + s.text
