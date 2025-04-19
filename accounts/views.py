from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Activity_Contact, Course_Contact, Product_Contact, TakeOrder 
from .models import ShoppingCart

# Create your views here.
def register_login(request):
    # add code of register and login

    return render(request, 'accounts/register_login.html')
	
def dashboard(request):
    activity_contacts = Activity_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    course_contacts = Course_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    product_contacts = Product_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    takeOrders = TakeOrder.objects.order_by('-contact_date').filter(user_id=request.user.id)
    #shoppingcarts = ShoppingCart.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {'activity_contacts' : activity_contacts, 'course_contacts' : course_contacts, 'product_contacts' : product_contacts, 'takeOrders' : takeOrders} #, 'shoppingcarts' : shoppingcarts}

    return render(request, 'accounts/dashboard.html' , context)

def shoppingCart(request):
    shoppingCarts = ShoppingCart.objects.order_by('-contact_date').filter(user_id=request.user.id)
    takeOrders = TakeOrder.objects.order_by('-contact_date').filter(user_id=request.user.id)
    #for takeOrder in takeOrders:
    context = {'shoppingCarts' : shoppingCarts, 'takeOrders' : takeOrders}

    return render(request, 'partials/_shoppingCart.html', context)