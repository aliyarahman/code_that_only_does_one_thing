# Section 1: Go get the tools so you can do requests and pretend you're a browser that speaks HTTP
import requests
import pprint	# Import the pretty-print data reader			
from settings_hidden import API_KEY

# Note: you will need to make a file in the same directory as this called 'settings_hidden.py' . It should have the following line of code:
# API_KEY = 'whatever-your-api-key-is'

address = raw_input("Please enter an address: ")

url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+API_KEY

r = requests.get(url)
results = r.json()		# Save your answer to results

lat = results['results'][0]['geometry']['location']['lat']
lng = results['results'][0]['geometry']['location']['lng']

print "\nLatitude: "+str(lat)
print "Longitude: "+str(lng)+"\n"
