from django.http import HttpResponse
from django.shortcuts import render

from greenvasadev.settings import BASE_DIR

from seller.models import Product_List
from sign_up_in.models import G_Sign_up

G_Sign_up

# Create your views here.

def index(request):
    request.session["login_status"]=False
    return render(request,'landing.html')


def products(request):
    product = Product_List.objects.all()
    print(type(product))
    print(len(product))
    print(BASE_DIR)
    print(product[0].product_image1)
    print(product[0].id)
    print(product[1].id)
    return render(request,'products.html', {'products': product, 'BASE_DIR':BASE_DIR})

def product_details(request, id):
    product = Product_List.objects.get(id=id)
    user_name = product.user_id
    seller_details = G_Sign_up.objects.get(email=user_name)

    return render(request,'products_details.html', {'product': product, 'seller_details':seller_details, 'BASE_DIR':BASE_DIR})