import csv
from app.models import Thread, Forum, UserProfile, Post
from django.contrib.auth.models import User

# Open the csv we're reading from
with open('commotion-discuss.txt_sorted.csv', 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
'''	# Add forums
	forums = []
	for index, row in enumerate(forum_data_reader):
		if index >0:
			if row[1] not in forums:
				forums.append(row[1])
	for forum in forums:
		f = Forum(title = forum)
		f.save()'''
	# Add users
	users = []
	for index, row in enumerate(forum_data_reader):
		if index >0:
			if row[5] not in users:
				users.append(row[5])
	for user in users:
		try:
			firstname = user.split(" ")[0]
			lastname = user.split(" ")[1]
		except:
			firstname = "Unknown"
			lastname = "User"
		u = User(first_name = firstname, last_name = lastname, username = user, password="default123", email="default@forum.com")
		u.save()

			# Add threads



			# Add messages