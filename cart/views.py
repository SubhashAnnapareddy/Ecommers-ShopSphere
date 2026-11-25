from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from base.models import Product
from django.http import JsonResponse
# Create your views here.
def add_to_cart(request,pk):
    product=get_object_or_404(Product,id=pk)
    try:
        cart_product=get_object_or_404(Cart,product=product)
        cart_product.quantity+=1
        cart_product.save()
    except:
        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            total_price=product.price
        )
    return redirect('home')

def cartpage(request):
    cart_products=Cart.objects.filter(user=request.user)
    TA=0
    for i in Cart.objects.filter(user=request.user):
        TA+=i.total_price
    # print(TA)
    return render(request,'cartpage.html',{'cart_products':cart_products,'TA':TA})

def remove(request,pk):
    get_object_or_404(Cart,id=pk).delete()
    return redirect('cartpage')

def plus(request,pk):
    cart_product=get_object_or_404(Cart,id=pk)
    cart_product.quantity+=1
    cart_product.total_price+=cart_product.product.price
    cart_product.save()
    return redirect('cartpage')

def minus(request,pk):
    cart_product=get_object_or_404(Cart,id=pk)
    if cart_product.quantity>1:
        cart_product.quantity-=1
        cart_product.total_price-=cart_product.product.price
        cart_product.save()
    else:
        cart_product.delete()
    return redirect('cartpage')
