import csv

#Open the raw text file
filename = "commotion-discuss.txt"
with open(filename, "r") as archive_file:
	content = archive_file.readlines()


# Create a list of starting line indexes to use later
# Improved performance so that conditionals for subject etc are not checking more lines than necessary
counter = 0
start_indexes = []
for index, row in enumerate(content):
	if "From " in row[0:5]:
		start_indexes.append(index)

# Assemble the csv by writing id, start_line, username, datetime, subject, full_username
with open(filename+'_sorted'+'.csv', 'wb') as csvfile:
	archivewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	archivewriter.writerow(["message_number", "starting_line", "ending_line", "message_content"])
	for index, start_line in enumerate(start_indexes):
		username_is_in = content[start_line]
		full_name_is_in = content[start_line+1]
		datetime_is_in = content[start_line+2]
		timezone_is_in = content[start_line+2]
		subject_is_in = content[start_line+3]
		try:
			end_line = start_indexes[index+1]-1
		except:
			end_line = len(content)
		message_content = content[start_line+4:end_line]
		archivewriter.writerow([index, start_line, end_line, message_content])
