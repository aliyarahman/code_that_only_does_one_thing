import csv
#Python uses 'packages' to hold a set of tools you don't use all the
#time. But you can import them when you need them. CSV is a package of tools for
#working on CSVs.


with open('the_file_name.csv', 'rb') as csvfile:
	event_file_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in event_file_reader:
		print row[0], row[1]


# Working with a csv file always has these parts:
#---------------------------------------------------
# A line (like line 7) to open the file that tells the computer which file 
# you want to open and some options to help it understand how that file is laid out.

# A line (like line 8) that tells Python how to save the info from the csv in its own
# language.

# A line (like line 9) that starts the for loop that will cycle through all the rows

# Then, the print line prints out the value from the first and second columns for each row
