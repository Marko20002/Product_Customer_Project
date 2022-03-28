from django.db import models

class Product(models.Model):
	name 		=models.CharField(max_length=100)
	my_choices=(
		('a','тренерки'),
		('b','пижами'),
		('c','блузи')
		)
	my_choices1=(
		('a','S'),
		('b','M'),
		('c','L'),
		('d','XL')
		)
	my_choices2=(
		('a','MKD'),
		('b','USD'),
		('c','EUR')
		)
	my_field	=models.CharField(max_length=1,choices=my_choices)
	kolicina 	=models.IntegerField()
	velicina  	=models.CharField(max_length=1,choices=my_choices1)
	valuta		=models.CharField(max_length=1,choices=my_choices2)
	price  		=models.DecimalField(decimal_places=2,max_digits=10000)
