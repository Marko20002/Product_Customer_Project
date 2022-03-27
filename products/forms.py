from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
	class Meta:
		model = Product
		fields= [
		'name',
		'my_field',
		'kolicina',
		'velicina',
		'price'
		]