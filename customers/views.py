from django.shortcuts import render

# Create your views here.
from .forms import AddCustomers
from .models import Customers

def add_customer(request):
	form1=AddCustomers(request.POST or None)
	if form1.is_valid():
		form1.save()
		form1=AddCustomers()
	context={
		'form1':form1
	}
	return render(request,"customers/add_customer.html",context)

