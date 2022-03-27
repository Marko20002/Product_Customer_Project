from django.shortcuts import render, get_object_or_404

from .forms import ProductCreateForm
from .models import Product



def product_create(request):
	form=ProductCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductCreateForm()
	context={
		'form':form
	}
	return render(request,"products/product_create.html",context)


def delete_product(request,id):	
	obj=Product.objects.get(id=id)
	try:
		obj.delete()
	except Product.DoesNotExist:
  		raise Http404("There is no such product")
  	
	return render(request,"products/product_delete.html")