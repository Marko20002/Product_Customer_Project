from django import forms

from .models import Customers

class AddCustomers(forms.ModelForm):
	class Meta:
		model = Customers
		fields= [
		'name',
		'surname', 			
		'email', 				
		'credit_card', 					
		'address',  			
		'number_of_adress',	
		'Postal_code',			
		'city', 			
		'country_name'
		]