from django.shortcuts import render

# Create your views here.
from .forms import AddCustomers
from .models import Customers

def add_customer(request):
	form1=AddCustomers(request.POST or None)
	if form1.is_valid():
		cleaned_info=form1.cleaned_data
		credit=cleaned_info['credit_card']
		if(credit[0]=='4'or credit[0]=='5' or credit[0]=='6' ):
			if(len(credit)==16):
				ff=True
				for i in range(16):
					if credit[i]>='0'and credit[i]<='9':
						if i>=3:
							f=False
							for j in range(4):
								if(credit[i-j]!=credit[i]):
									f=True
							if(f==False):

								ff=False
								break
					else:
						ff=False
				if(ff):		


					form1.save()
					form1=AddCustomers()
	context={
		'form1':form1
	}
	return render(request,"customers/add_customer.html",context)


def delete_customer(request,id):	
	obj=Customers.objects.get(id=id)
	try:
		obj.delete()
	except Product.DoesNotExist:
  		raise Http404("There is no such product")
  	
	return render(request,"customers/delete_customer.html")