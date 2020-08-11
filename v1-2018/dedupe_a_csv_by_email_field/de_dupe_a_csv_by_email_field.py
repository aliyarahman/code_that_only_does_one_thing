import csv # import the basic Python CSV module

# Load your input file into a variable and create a blank csv file to output
input_file = 'volunteer.csv'
output_file = 'volunteer_deduped.csv'

# Loop through the csv
with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
    reader = csv.reader(file_in) # Make a variable
    writer = csv.writer(file_out)
    d = [] # Make an empty list where you can store names we've already seen
    for row in reader: # oh!!!!! a for loop!!!!
        email = row[7] # if we want to dedupe by email and the email is in column C of the csv, for example
        if email not in d:
            d.append(email)
            writer.writerow(row)


        
