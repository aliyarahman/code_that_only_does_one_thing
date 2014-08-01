Code That Only Does One Thing
=============================

Directories in this repository hold stand-alone code clusters that demonstrate bare-bones functionalities available in Python 2.7, Flask, Django, and libraries intended for use with them.

Generally, a requirements.txt file is included to document dependencies installed on the virtual environment.



Contents
--------
**add basic svg shapes**: Sets up an svg canvas on a page and adds a circle and a square

**call a sunlight api**: Calls the Sunlight API to look for a phrase that the user specifies. Prints it our pretty with prettyprint.

**call the Salesforce api**: Calls the Salesforce API and makes a query to find people signed up for housing alerts using the Python SimpleSalesforce package.

**call the twitter api**: Calls the Twitter API and asks for all the recent Tweets that mention #yesallwomen

**launch a Flask app with a bare bones skeleton**: Launches an app that says 'Hello, world' in the browser, but has the full (yet bare) skeleton that larger apps will need.

**make a widget using an iframe**: Shows the mechanics of widgetizing an existing Django app.

**read a csv**: Uses Python's csv package to open a .csv file and print out values in its first two columns for every row in that file

**run a unit test**: A example of the flow of test-driven development using the Python unittest module

**scrape a web page with Beautiful Soup**: A simple use of BeautifulSoup to scrape links from an article about women DJs.

**scrape email archives with lxml**: Looks at a table of a list's mailman archives, downloads each archive and unzips if necessary, puts all contents into one long text file

**send a text message in twilio**: Send a basic text message to one number using the Twilio REST API

**use a simple django form**: Lets the user, without logging in, enter a zip code into a single-field form, looks up service providers who match that zip code in a Postgres database, and spits out the results onto a second view.

