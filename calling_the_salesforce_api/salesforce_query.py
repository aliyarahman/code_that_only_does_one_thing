# Import the tools we need
from simple_salesforce import Salesforce

# Connect and authenticate
sf = Salesforce(instance='domain_name.salesforce.com', session_id='')

# Make a query to find the contacts who are signed up to receive housing alerts
people_to_text = sf.query("SELECT Id, Phone, FROM Contact WHERE LookingForHousing = True")

