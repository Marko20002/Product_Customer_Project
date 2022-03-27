from django.db import models

# Create your models here.
class Customers(models.Model):
	name 				=models.CharField(max_length=100)
	surname 			=models.CharField(max_length=100)
	email 				=models.EmailField(blank=True)
	credit_card 		=models.CharField(max_length=16)
	date_time 			=models.DateTimeField(auto_now=True)
	address  			=models.CharField(max_length=100)
	number_of_adress	=models.IntegerField()
	Postal_code			=models.IntegerField()
	city 				=models.CharField(max_length=100)
	country_name  		=models.CharField(max_length=100)
