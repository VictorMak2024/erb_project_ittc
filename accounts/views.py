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
def register_login(request):
    # add code of register and login

    return render(request, 'accounts/register_login.html')
	
def dashboard(request):
    activity_contacts = Activity_Contact.objects.filter(activity__salesmen__id=request.user.id).order_by('-contact_date')
    activities = Activity.objects.all()

    course_contacts = Course_Contact.objects.filter(course__salesmen__id=request.user.id).order_by('-contact_date')
    courses = Course.objects.all()

    product_contacts = Product_Contact.objects.filter(product__salesmen__id=request.user.id).order_by('-contact_date')
    products = Product.objects.all()

    takeOrders = TakeOrder.objects.all()

    shoppingCarts = ShoppingCart.objects.all()

    context = {'activity_contacts' : activity_contacts, 'course_contacts' : course_contacts, 'takeOrders' : takeOrders, 'product_contacts' : product_contacts, 'activities' : activities, 'courses' : courses, 'products' :products, 'shoppingCarts' : shoppingCarts}

    return render(request, 'accounts/dashboard.html' , context)

def shoppingCart(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to view your shopping cart.")
        return redirect('login')

    # Retrieve or create a shopping cart for the user
    shopping_cart, created = ShoppingCart.objects.get_or_create(user_id=request.user.id)

    # Get all TakeOrder entries for the user
    takeOrders = TakeOrder.objects.filter(user_id=request.user.id)

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

def confirmOrder(request):
    if request.method == 'POST':
        address = request.POST['address']
        street = request.POST['street']
        district = request.POST['district']
        user_id = request.POST['user_id']
        is_paid = request.POST['is_paid']
        description = request.POST['description']

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

        messages.success(request, "Your order has been confirmed!")
        return redirect('shoppingCart')
    
# def confirmOrder(request):
#     if request.method == 'POST':
#         #orders = request.POST.get['orders']
#         address = request.POST['address']
#         street = request.POST['street']
#         district = request.POST['district']
#         user_id = request.POST['user_id']
#         is_paid = request.POST['is_paid']
#         total_Amount = int(request.POST['total_Amount'])
#         #salesmen_id = request.POST['salesmen_id']
#                 # Validate that required fields are provided
#         orders = shopping_cart.orderes.add(request.POST.getlist('orders'))

#         if not orders or not user_id:
#             messages.error(request, "Missing required fields to confirm the order.")
#             return redirect('shoppingCart')
#         # Retrieve the user's shopping cart
#         shopping_cart = ShoppingCart.objects.filter(user_id=user_id).first()
#         if not shopping_cart:
#             messages.error(request, "Shopping cart not found.")
#             return redirect('shoppingCart')

#         # Check if the order already exists
#         existing_order = ShoppingCart.objects.filter(orders=orders, user_id=user_id).first()
#         if existing_order:
#             messages.error(request, "You have already placed this order. Please check the shipment status!")
#             return redirect('shoppingCart')

#         # Save the confirmed order
#         shopping_cart.address = address
#         shopping_cart.street = street
#         shopping_cart.district = district
#         shopping_cart.user_id = user_id
#         shopping_cart.is_paid = is_paid
#         shopping_cart.total_Amount = total_Amount
#         shopping_cart.orders.add(orders)
#         shopping_cart.save()
        

#         messages.success(request, "Your order has been confirmed!")
#         return redirect('shoppingCart')

#         # takeOrder = get_object_or_404(TakeOrder, pk=user_id)
#         # # Check if the user already has this product in their cart
#         # confirm_order = shoppingCart.Order.objects.filter(orders=orders, user_id=user_id).first()
#         # if confirm_order:
#         #     messages.Wrong(request, "YOu had placed order before. Please checking the order shippment status!")
    
#         # else:
#         #     confirm_order = ShoppingCart(orders=orders(takeOrder), name=name, address=address, street=street, district=district, user_id=user_id, is_paid=is_paid)
#         #     confirm_order.save()

#         # # Add the order to the user's shopping cart
#         # #shopping_cart.created = ShoppingCart.objects.get_or_create(user_id=user_id)
#         # #shopping_cart.orders.add(takeOrder)

#         # messages.success(request, "This product has been added to your shopping cart!")
#     return redirect('/shoppingCart/')
# # def shoppingCart(request):
# #     # shoppingCarts = ShoppingCart.objects.order_by('-contact_date').filter(user_id=request.user.id)
# #     takeOrders = TakeOrder.objects.order_by('-contact_date').filter(user_id=request.user.id)
# #     #for takeOrder in takeOrders:
    
    
# #     # if request.method == 'POST':
#     #     product_id = request.POST['product_id']
#     #     product = request.POST['product']
#     #     product_title = request.POST['product_title']
#     #     name = request.POST['name']
#     #     price = request.POST['price']
#     #     onOrderQty = request.POST['onOrderQty']
#     #     user_id = request.POST['user_id']
#     #     salesmen_id = request.POST['salesmen_id']
#     #     if request.user.is_authenticated:
#     #         #user_id = request.user.id
#     #         has_contacted = TakeOrder.objects.all().filter(product_id=product_id, user_id=user_id)
#     #         if has_contacted:
#     #             messages.error(request, "You have already made an inquiry for this product at this time !")
#     #             return redirect('/products/'+product_id)
#     #     takeOrder = TakeOrder(product_id=product_id,  product=product, product_title=product_title, price=price, name=name, onOrderQty=onOrderQty, user_id=user_id, salesmen_id=salesmen_id)
#    #  takeOrder.save()

#     #    messages.success(request, "This product has been added to your shopping cart!")

#     context = {'takeOrders' : takeOrders}

#     #return redirect(request, 'shoppingCart,html', context)'shoppingCarts' : shoppingCarts, 
#     return render(request, 'partials/_shoppingCart.html', context)
# # def search(request):
# #     queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True) 
# #     if 'keywords' in request.GET:
# #         keywords = request.GET['keywords']
# #         if keywords:
# #             queryset_list = queryset_list.filter(description__icontains=keywords)
# #     if 'title' in request.GET:
# #         title = request.GET['title']
# #         if title:
# #             queryset_list = queryset_list.filter(title__icontains=title)
# #     if 'district' in request.GET:
# #         district = request.GET['district']
# #         if district:
# #             #queryset_list = queryset_list.filter(district__icontains=district)
# #             queryset_list = queryset_list.filter(district__iexact=district)
# #     if 'price' in request.GET:
# #         price = request.GET['price']
# #         if price:
# #             queryset_list = queryset_list.filter(price__lte=price)
# #     if 'bedrooms' in request.GET:
# #         bedrooms = request.GET['bedrooms']
# #         if bedrooms:
# #             queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

# #     paginator = Paginator(queryset_list, 3)
# #     page = request.GET.get('page')
# #     paged_listings = paginator.get_page(page)
# #     values = request.GET.copy()
# #     if 'page' in values:
# #         del values["page"]

# #     context = {
# #         "price_choices" : price_choices,
# #         "bedroom_choices" : bedroom_choices,
# #         "district_choices" : district_choices,
# #         #"listings" : queryset_list,
# #         "listings" :paged_listings,
# #         "values" : values
# #         }
# #     return render(request, 'listings/search.html', context)
# # 
# # def delete_take(request, takeOrder_id):
# #     contact = get_object_or_404(TakeOrder, pk=takeOrder_id)
# #     contact.delete()
# #     return redirect('shoppingCart')

# def shoppingCart(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "You need to log in to view your shopping cart.")
#         return redirect('login')

#     # Retrieve or create a shopping cart for the user
# #    shoppingCart.created = ShoppingCart.objects.get_or_create(user_id=request.user.id)
#     shopping_cart, created = ShoppingCart.objects.get_or_create(user_id=request.user.id)

#     # Get all TakeOrder entries for the user
#     takeOrders = TakeOrder.objects.filter(user_id=request.user.id)

#     # Add all TakeOrder entries to the shopping cart / 'created' : created, 'orders': shopping_cart.orders.all(),
#     total_Amount =0
#     for takeOrder in takeOrders:
#         shopping_cart.orders.add(takeOrder)
#         total_Amount += takeOrder.amount
      
#        # total_Amount = shopping_cart.total_Amount +takeOrder.Amount
#       #  shopping_cart.total_Amount = total_Amount

#     context = {'shopping_cart': shopping_cart, 'takeOrders': takeOrders, "district_choices" : district_choices, 'total_Amount': total_Amount }
#     return render(request, 'partials/_shoppingCart.html', context)
