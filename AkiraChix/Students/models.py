from django.db import models

# Create your models here.

class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DateField()
	registration_number=models.CharField(max_length=30)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=15)
	gmail=models.EmailField()
	guardian_name=models.CharField(max_length=30)
	id_number=models.IntegerField(max_length=10)
	date_joined=models.DateField()



