from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Activity_Contact, Course_Contact, Product_Contact, TakeOrder 
from activities.models import Activity
from courses.models import Course
from products.models import Product
from .models import ShoppingCart

# Create your views here.
def register_login(request):
    # add code of register and login

    return render(request, 'accounts/register_login.html')
	
def dashboard(request):
    activity_contacts = Activity_Contact.objects.filter(activity__salesmen__id=request.user.id).order_by('-contact_date')
    activities = Activity.objects.all()
    #activity_contacts = Activity_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    course_contacts = Course_Contact.objects.filter(crouse__salesmen__id=request.user.id).order_by('-contact_date')
    courses = Course.objects.all()#course_contacts = Course_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    product_contacts = Product_Contact.objects.filter(product__salesmen__id=request.user.id).order_by('-contact_date')
    products = Product.objects.all()#product_contacts = Product_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    takeOrders = TakeOrder.objects.filter(takeOrder__salesmen__id=request.user.id).order_by('-contact_date')
    #takeOrders = TakeOrder.objects.all()
    #takeOrders = TakeOrder.objects.order_by('-contact_date').filter(user_id=request.user.id)
    #shoppingcarts = ShoppingCart.objects.order_by('-contact_date').filter(user_id=request.user.id)

    # activities = Activity.objects.filter()
    # courses = Course.objects.all()
    # products = Product.objects.all()
    
    context = {'activity_contacts' : activity_contacts, 'course_contacts' : course_contacts, 'takeOrders' : takeOrders, 'product_contacts' : product_contacts, 'activities' : activities, 'courses' : courses, 'products' :products } #, 'shoppingcarts' : shoppingcarts}'course_contacts' : course_contacts, 'takeOrders' : takeOrders,

    return render(request, 'accounts/dashboard.html' , context)

def shoppingCart(request):
    # shoppingCarts = ShoppingCart.objects.order_by('-contact_date').filter(user_id=request.user.id)
    takeOrders = TakeOrder.objects.order_by('-contact_date').filter(user_id=request.user.id)
    #for takeOrder in takeOrders:
    
    
    # if request.method == 'POST':
    #     product_id = request.POST['product_id']
    #     product = request.POST['product']
    #     product_title = request.POST['product_title']
    #     name = request.POST['name']
    #     price = request.POST['price']
    #     onOrderQty = request.POST['onOrderQty']
    #     user_id = request.POST['user_id']
    #     salesmen_id = request.POST['salesmen_id']
    #     if request.user.is_authenticated:
    #         #user_id = request.user.id
    #         has_contacted = TakeOrder.objects.all().filter(product_id=product_id, user_id=user_id)
    #         if has_contacted:
    #             messages.error(request, "You have already made an inquiry for this product at this time !")
    #             return redirect('/products/'+product_id)
    #     takeOrder = TakeOrder(product_id=product_id,  product=product, product_title=product_title, price=price, name=name, onOrderQty=onOrderQty, user_id=user_id, salesmen_id=salesmen_id)
   #  takeOrder.save()

    #    messages.success(request, "This product has been added to your shopping cart!")

    context = {'takeOrders' : takeOrders}

    #return redirect(request, 'shoppingCart,html', context)'shoppingCarts' : shoppingCarts, 
    return render(request, 'partials/_shoppingCart.html', context)
# def search(request):
#     queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True) 
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords:
#             queryset_list = queryset_list.filter(description__icontains=keywords)
#     if 'title' in request.GET:
#         title = request.GET['title']
#         if title:
#             queryset_list = queryset_list.filter(title__icontains=title)
#     if 'district' in request.GET:
#         district = request.GET['district']
#         if district:
#             #queryset_list = queryset_list.filter(district__icontains=district)
#             queryset_list = queryset_list.filter(district__iexact=district)
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             queryset_list = queryset_list.filter(price__lte=price)
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

#     paginator = Paginator(queryset_list, 3)
#     page = request.GET.get('page')
#     paged_listings = paginator.get_page(page)
#     values = request.GET.copy()
#     if 'page' in values:
#         del values["page"]

#     context = {
#         "price_choices" : price_choices,
#         "bedroom_choices" : bedroom_choices,
#         "district_choices" : district_choices,
#         #"listings" : queryset_list,
#         "listings" :paged_listings,
#         "values" : values
#         }
#     return render(request, 'listings/search.html', context)
def delete_take(request, takeOrder_id):
    contact = get_object_or_404(TakeOrder, pk=takeOrder_id)
    contact.delete()
    return redirect('shoppingCart')