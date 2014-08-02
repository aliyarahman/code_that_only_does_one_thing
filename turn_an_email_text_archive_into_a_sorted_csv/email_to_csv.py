#Open the file
with open("commotion-discuss.txt", "r") as archive_file:
	content = archive_file.readlines()

#  Find the indexes for all of the messages' starting lines
counter = 0
start_indexes = []
for index, row in enumerate(content):
	if "From " in row[0:5]:
		start_indexes.append(index)
		counter +=1

print counter
print start_indexes