from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from greenvasadev.settings import BASE_DIR

from seller.models import Product_List, Approved_Product_List
from sign_up_in.models import G_Sign_up

G_Sign_up

# Create your views here.

def index(request):
    request.session["login_status"]=False
    login_status = request.session["login_status"]
    return render(request,'landing.html')

def aboutUs(request):
    # request.session["login_status"]=False
    return render(request,'about_us.html')

def products(request):
    product = Approved_Product_List.objects.all()
    print(type(product))
    print(len(product))
    print(BASE_DIR)
    # print(product[0].product_image1)
    # print(product[0].id)
    # print(product[1].id)
    return render(request,'products.html', {'products': product, 'BASE_DIR':BASE_DIR})


@staff_member_required(login_url='/admin')
def products_admin(request):
    product = Product_List.objects.all()
    print(type(product))
    print(len(product))
    print(BASE_DIR)
    # print(product[0].product_image1)
    # print(product[0].id)
    # print(product[1].id)
    return render(request,'products_admin.html', {'products': product, 'BASE_DIR':BASE_DIR})

# @staff_member_required(login_url='/admin')
def product_details(request, id):
    product = Approved_Product_List.objects.get(id=id)
    user_name = product.user_id
    seller_details = G_Sign_up.objects.get(email=user_name)

    return render(request,'products_details.html', {'product': product, 'seller_details':seller_details, 'BASE_DIR':BASE_DIR})


@staff_member_required(login_url='/admin')
def product_details_admin(request, id):
    product = Product_List.objects.get(id=id)
    user_name = product.user_id
    seller_details = G_Sign_up.objects.get(email=user_name)

    if request.method == 'POST':
        product_Table = Approved_Product_List()
        product_Table.user_id = product.user_id
        product_Table.product_name = product.product_name
        product_Table.product_description = product.product_description
        product_Table.expected_price = product.expected_price
        product_Table.category = product.category
        product_Table.product_image1 = product.product_image1
        product_Table.product_image2 = product.product_image2
        product_Table.product_image3 = product.product_image3
        product_Table.product_image4 = product.product_image4

        product_Table.save()
        ap_product = Product_List(id=product.id)
        ap_product.delete()
        return redirect('main:admin_products')

    return render(request,'products_details_admin.html', {'product': product, 'seller_details':seller_details, 'BASE_DIR':BASE_DIR})