"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import product_create, delete_product, product_list
from customers.views import add_customer, delete_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createproduct/', product_create),
    path('deleteproduct/<int:id>/', delete_product),
    path('deletecustomer/<int:id>/', delete_customer),
    path('addcustomer/', add_customer),
    path('listofproducts/', product_list),
    
]
