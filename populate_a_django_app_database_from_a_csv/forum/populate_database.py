import csv
from app.models import Thread, Forum, UserProfile, Post
from django.contrib.auth.models import User

# Open the csv we're reading from
with open('commotion-discuss.txt_sorted.csv', 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	# Add forums
	forums = []
	for index, row in enumerate(forum_data_reader):
		if index >0:
			if row[1] not in forums:
				forums.append(row[1])
	for forum in forums:
		f = Forum(title = forum)
		f.save()


#### Note need to correct user password creation
with open('commotion-discuss.txt_sorted.csv', 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
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
		u = User.objects.create_user(first_name = firstname, last_name = lastname, username = user, password="default123", email="default@forum.com")
		u.save()

with open('commotion-discuss.txt_sorted.csv', 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		# Add threads
	threads = []
	for index, row in enumerate(forum_data_reader):
		if index >0:
			if row[2] not in threads:
				threads.append(row[2])
				creator = User.objects.filter(username = row[5]).first()
				forum = Forum.objects.filter(title=row[1]).first()
				title = row[2]
				t = Thread(title =title, creator = creator, forum = forum)
				t.save()

# Add posts
with open('commotion-discuss.txt_sorted.csv', 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for index, row in enumerate(forum_data_reader):
		if index >0:
			creator = User.objects.filter(username = row[5]).first()
			thread = Thread.objects.filter(title = row[2]).first()
			p = Post(creator=creator, thread=thread, title="", body=row[6])
			p.save()