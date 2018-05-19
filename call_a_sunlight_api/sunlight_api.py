# Section 1: Go get the tools so you can do requests and speak HTTP
import requests
import pprint	# Import the pretty-print data reader			


# Section 2: Ask the user what search term they want to look up?
search_term = raw_input("What phrase do you want to look up?: ")

# Section 2: Make the API call - ask it a question and save the answer in the r variable
# NOTE you need to enter your own API key to the end of the url below
api_key = 'whatever_your_api_key_is'
url = 'http://capitolwords.org/api/1/phrases/legislator.json?phrase='+search_term+'&page=0&per_page=50&sort=count&apikey='+api_key
r = requests.get(url)

# Section 3: Print out the answer we got from the API, in json format
results = r.json()		# Save your answer to results

# Print it prettier

legislator_id = results['results'][0]['legislator']

print legislator_id


# Section 4: Find out who this actually is
r = requests.get('http://congress.api.sunlightfoundation.com/legislators?bioguide_id='+legislator_id+'&apikey=whatever_your_api_key_is')
legislator_result = r.json()

say_this = legislator_result['results'][0]['first_name']+" "+legislator_result['results'][0]['last_name']+ " said lots of stuff about "+search_term+"."

print say_this
