import csv

#Open the file
filename = "commotion-discuss.txt"
with open(filename, "r") as archive_file:
	content = archive_file.readlines()

#  Find the indexes for all of the messages' starting lines
counter = 0
start_indexes = []


with open(filename+'_sorted'+'.csv', 'wb') as csvfile:
	archivewriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	archivewriter.writerow(["message_number", "starting_line"])
	for index, row in enumerate(content):
		if "From " in row[0:5]:
			counter +=1
			archivewriter.writerow([counter, index])