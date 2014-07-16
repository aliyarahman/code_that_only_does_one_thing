This app holds two views only for the sake of showing how a form that does not commit data to a database can pass along data as a query parameter.

(1) One with a form that prompts the user to enter their zipcode.

(2) One that displays the service providers in the zipcode entered by the user, using a database call.

Data is retrieved from a single-table Postgres database that holds name and zip for service providers.

Users do not need to log in to use the form.
