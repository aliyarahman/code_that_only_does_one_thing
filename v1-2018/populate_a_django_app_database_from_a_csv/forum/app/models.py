from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models import CharField, DateTimeField, ForeignKey, TextField, ImageField, IntegerField, OneToOneField


class Forum(models.Model):
	title = CharField(max_length=60)

	def __unicode__(self):
		return self.title


class Thread(models.Model):
	title = CharField(max_length=60)
	created = DateTimeField(auto_now_add=True)
	creator = ForeignKey(User, blank=True, null=True)
	forum = ForeignKey(Forum, related_name="threads")

	def __unicode__(self):
		return unicode("Thread: %s" % (self.title))


class Post(models.Model):
	title = CharField(max_length=60)
	created = DateTimeField(auto_now_add=True)
	creator = ForeignKey(User, blank=True, null=True)
	thread = ForeignKey(Thread, related_name="posts")
	body = TextField(max_length=10000)

	def __unicode__(self):
		return u" %s - %s" % (self.thread, self.title)


class UserProfile(models.Model):
	avatar = ImageField("Profile Pic", upload_to="images/", blank=True, null=True)
	posts = IntegerField(default=0)
	user = OneToOneField(User, related_name="profile")

	def __unicode__(self):
		return unicode(self.user)