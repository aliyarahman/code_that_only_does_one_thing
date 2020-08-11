from django.db import models


# Create your models here.

class Center(models.Model):
	center_code = models.CharField(max_length=40)
	five_digit_zip = models.IntegerField() #If we say only the first five numbers, we can store as an integer
