from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from cart.models import *
from django.contrib import messages
# Create your views here.
def add_address(request):
    form=AddressForm()
    if request.method=='POST':
        form_data=AddressForm(request.POST)
        if form_data.is_valid():
            a=form_data.save(commit=False)
            a.user=request.user
            a.save()
            return redirect('address_list')
    context={'form':form}
    return render(request,'add_address.html',context)

def address_list(request):
    address=Address.objects.all()
    return render(request,'address_list.html',{'address':address})

def update_address(request,pk):
    address=Address.objects.get(id=pk)
    if request.method=='POST':
        form=AddressForm(request.POST,instance=address)
        if form.is_valid():
            a=form.save(commit=False)
            a.user=request.user
            a.save()
            return redirect('address_list')
    else:
        form=AddressForm(instance=address)
        context={'form':form}
    return render(request,'update_address.html',context)
        
def checkout(request):
    addresses=Address.objects.filter(user=request.user)
    cart_items=Cart.objects.filter(user=request.user)
    # TA=0
    # for i in cart_product:
    #     TA+=i.total_price
    grand_total=sum(i.total_price for i in cart_items)
    context={
        'cart_items':cart_items,
        'addresses':addresses,
        'grand_total':grand_total
    }
    return render(request,'checkout.html',context)

def place_order(request):
    if request.method == 'POST':
        try:
            address = Address.objects.get(id=request.POST['address'], user=request.user)
        except:
            address = Address.objects.filter(is_default=True, user=request.user).first()

        cart_product = Cart.objects.filter(user=request.user)
        grand_price = sum(i.total_price for i in cart_product)

        order = Order.objects.create(
            user=request.user,
            address=address,
            total_amount=grand_price
        )

        for i in cart_product:
            OrderItem.objects.create(
                order=order,
                product=i.product,
                price=i.product.price,
                quantity=i.quantity
            )

            i.product.stock -= i.quantity
            i.product.save()

        cart_product.delete()

        messages.success(request, 'Your Order has been placed Successfully...!')
        return redirect('order_success', order.id)

    return redirect('order_success',order.id)

def order_success(request,pk):
    order_product=Order.objects.get(id=pk)
    return render(request,'order_success.html',{'order_product':order_product})

def order_details(request,pk):
    order=get_object_or_404(Order,id=pk,user=request.user)
    items=order.items.all()
    items=order.items.select_related('product')
    print(items)
    context={'order':order,'items':items}
    return render(request,'order_details.html',context)

def order_history(request):
    orders=Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'order_history.html',{'orders':orders})