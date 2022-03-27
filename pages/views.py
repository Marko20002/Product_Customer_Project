from django.http import HttpResponse
from django.shortcuts import render
	

def create_product(request,*args,**kwargs):

	return render(request,"create_product.html",{})
def add_customer(request,*args,**kwargs):

	return render(request,"add_customer.html",{})