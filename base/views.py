from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.db.models import Q
from django.contrib import messages
def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        # category=Category.objects.filter(cname__icontains=q)
        # cat=category[]
        all_products=Product.objects.filter(Q(pname__icontains=q)&Q(is_delete=False)).order_by('?')
        if len(all_products)==0:
            messages.error(request,'No Products..!')
            return redirect('home')
    elif 'cat' in request.GET:
        cat=request.GET['cat']
        cat_data=Category.objects.get(cname=cat)
        all_products=Product.objects.filter(category=cat_data.id)
    else:
        all_products = Product.objects.filter(is_delete=False).order_by('?')

    category =[]
    for i in Category.objects.all():
        if i.cname not in category:
            category.append(i.cname)

    return render(request,'home.html',{'all_products':all_products,'category':category,'nav':True})


def details(request,pk):
    product = get_object_or_404(Product,id=pk)
    category_product=Product.objects.filter(category=product.category).order_by('?').exclude(id=pk)
    return render(request,'details.html',{'product':product,'category_product':category_product})