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
        new_rowemail = [row[0], row[2], row[1], row[3]]
        writer.writerow(new_row)