from django.contrib.auth.decorators import login_required
import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Activity_Contact, Course_Contact, Product_Contact, TakeOrder 
from activities.models import Activity
from courses.models import Course
from products.models import Product
from .models import ShoppingCart
from .choices import district_choices

# Create your views here.
def register(request):
    # add code of register
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'You are now registered and can log in')
                return redirect('register')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    # add code of login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            #messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # add code of logout
    if request.method == 'POST':
        auth.logout(request)
    return redirect('index')
def dashboard(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to view your dashboard.")
        return redirect('login')

    activity_contacts = Activity_Contact.objects.filter(activity__salesmen__id=request.user.id).order_by('-contact_date')
    course_contacts = Course_Contact.objects.filter(course__salesmen__id=request.user.id).order_by('-contact_date')
    product_contacts = Product_Contact.objects.filter(product__salesmen__id=request.user.id).order_by('-contact_date')
    takeOrders = TakeOrder.objects.filter(user_id=request.user.id)
    shoppingCarts = ShoppingCart.objects.filter(user_id=request.user.id)

    context = {
        'activity_contacts': activity_contacts,
        'course_contacts': course_contacts,
        'product_contacts': product_contacts,
        'takeOrders': takeOrders,
        'shoppingCarts': shoppingCarts,
    }

    return render(request, 'accounts/dashboard.html', context)

@login_required
def shoppingCartOrders(request):
    # Retrieve the shopping cart for the logged-in user
    shopping_cart = ShoppingCart.objects.filter(user_id=request.user.id).first()

    if not shopping_cart:
        messages.error(request, "You do not have any items in your shopping cart.")
        return redirect('dashboard')
    
    shipping_no = 10000 + shopping_cart.id

    # Retrieve all orders in the shopping cart
    orders = shopping_cart.orders.all()

    context = {
        'shopping_cart': shopping_cart,
        'orders': orders, 'shipping_no': shipping_no,
    }

    return render(request, 'accounts/shopping_cart_orders.html', context)

def shoppingCart(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to view your shopping cart.")
        return redirect('login')

    # Retrieve or create a shopping cart for the user
    shopping_cart, created = ShoppingCart.objects.get_or_create(user_id=request.user)

    # if shopping_cart is None:
    #     messages.error(request, "An error occurred while creating your shopping cart.")
    #     return redirect('dashboard')
    # Get all TakeOrder entries for the user
    takeOrders = TakeOrder.objects.filter(user_id=request.user.id, ordered=False)

    # Calculate the total amount
    total_Amount = 0
    for takeOrder in takeOrders:
        shopping_cart.orders.add(takeOrder)
        takeOrder.amount = takeOrder.price * takeOrder.onOrderQty
        takeOrder.save()

        total_Amount += takeOrder.amount

    # Update the shopping cart's total amount
    shopping_cart.total_Amount = total_Amount
    shopping_cart.save()

    context = {
        'shopping_cart': shopping_cart,
        'takeOrders': takeOrders,
        "district_choices": district_choices,
        'total_Amount': total_Amount,
    }
    return render(request, 'partials/_shoppingCart.html', context)


def remove_from_cart(request, order_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to modify your shopping cart.")
        return redirect('login')

    shopping_cart = get_object_or_404(ShoppingCart, user_id=request.user.id)
    order = get_object_or_404(TakeOrder, id=order_id)

    shopping_cart.orders.remove(order)
    messages.success(request, "Item removed from your shopping cart.")
    return redirect('shoppingCart')

logger = logging.getLogger(__name__)
def confirmOrder(request):
    if request.method == 'POST':
        address = request.POST['address']
        street = request.POST['street']
        district = request.POST['district']
        user_id = request.POST['user_id']
        is_paid = request.POST['is_paid']
        description = request.POST['description']
        ordered = request.POST['ordered']

        # Retrieve the user's shopping cart
        shopping_cart = ShoppingCart.objects.filter(user_id=user_id).first()
        if not shopping_cart:
            messages.error(request, "Shopping cart not found.")
            return redirect('shoppingCart')

        # Update shopping cart details
        shopping_cart.address = address
        shopping_cart.street = street
        shopping_cart.district = district
        shopping_cart.is_paid = is_paid
        shopping_cart.description = description
        shopping_cart.total_Amount = sum(
            order.price * order.onOrderQty for order in shopping_cart.orders.all()
        )
        shopping_cart.save()

        for order in shopping_cart.orders.all():
            product = order.product
            product.onOrderQty += order.onOrderQty  # Increment the product's onOrderQty
            product.save()
        
        messages.success(request, "Your order has been confirmed!")

        return redirect('shoppingCart')
    
