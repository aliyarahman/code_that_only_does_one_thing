# Section 1: Go get the tools you need for this script to work
import requests # allows you to speak HTTP
import pprint	# Import the pretty-print data reader			


# Section 2: Ask the user what state and search term they want to look up
state = raw_input("Which state's bills are you searching? Enter as the state's two-letter abbreviation in lower case letters (e.g. Wisconsin is wi): ")
search_term = raw_input("What phrase do you want to look for in those bills?: ")


# Section 2: Make the API call - ask it a question and save the answer in the r variable
# NOTE you need to enter your own API key to the end of the url below
api_key = '4a3c4db5-f1a1-46ea-b606-d8e26d4e7fe1'
url = 'https://openstates.org/api/v1/bills/?state='+state+'&q='+search_term+'&apikey='+api_key
r = requests.get(url)

# Section 3: Print out the answer we got from the API, in json format
results = r.json()		# Save your answer to results

# Print it prettier
pprint(results)