from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Activity_Contact, Course_Contact, Product_Contact, TakeOrder
from activities.models import Activity
from courses.models import Course
from products.models import Product
from accounts.models import ShoppingCart
from django.core.mail import send_mail

# Create your views here.
def activity_contact(request):
    if request.method == 'POST':
        activity_id = request.POST['activity_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        is_paid = request.POST['is_paid']
        salesmen_email = request.POST['salesmen_email']

        activity = get_object_or_404(Activity, pk=activity_id)

        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Activity_Contact.objects.all().filter(activity=activity, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already applied sitting for this activity !")
                return redirect('/activities/'+activity_id)
        
        activity_contact = Activity_Contact(activity=activity, name=name, email=email, phone=phone, message=message, user_id=user_id, is_paid=is_paid)
        activity_contact.save()
                #(activity=activity, 
        activitys = Activity.objects.get(id=activity_id)
        if activitys.onenquiry_sit == activitys.total_sit:
            messages.error(request, "Course is full",
            )
            return redirect('/activitys/'+activity_id)
        elif activitys.price != 0:
            messages.warning(request, f"You need to pay $"+str(activitys.price)+" for this activity to enroll. Once payment is done, you can proceed to enroll in this activity !")
        else:
            activitys.onenquiry_sit += 1
            activitys.save()

        # Send Email
        send_mail(
            'Activity Inquiry',
            f'There has been an inquiry for {activity.name}. Sign into the admin panel for more info.',
            #f'There has been an inquiry for '+activity+'. Sign into the admin panel for more info.',
            'nwcn0307@gmail.com', # admin email
            [salesmen_email], #to email
            fail_silently=False
        )
        messages.success(request, "Your request has been submitted, a direct sale will get back to you soon !")
    return redirect('/activities/'+activity_id)
    #return render(request, 'contacts/contact.html')

def course_contact(request):
    if request.method == 'POST':
        course_id = request.POST['course_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        is_paid = request.POST['is_paid']
        salesmen_email = request.POST['salesmen_email']

        course = get_object_or_404(Course, pk=course_id)
        
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Course_Contact.objects.all().filter(course= course, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already applied for this course !")
                return redirect('/courses/'+course_id)
        course_contact = Course_Contact(course=course, name=name, email=email, phone=phone, message=message, user_id=user_id, is_paid=is_paid)
        course_contact.save()

        courses = Course.objects.get(id=course_id)
        if courses.onenquiry_sit == courses.total_sit:
            messages.error(request, "Course is full")
            return redirect('/courses/'+course_id)
        elif courses.price != 0:
            messages.warning(request, f"You need to pay $"+str(courses.price)+" for this course to enroll. Once payment is done, you can proceed to enroll in this course !")
        else:
            courses.onenquiry_sit += 1
            courses.save()
        
        # Send Email
        send_mail(
            'Course Inquiry',
            f'There has been an inquiry for {course.name}. Sign into the admin panel for more info.',
            'nwcn0307@gmail.com', # admin email
            [salesmen_email], #to email
            fail_silently=False
        )
        messages.success(request, "Your request has been submitted, a direct sale will get back to you soon !")
    return redirect('/courses/'+course_id)
    #return render(request, 'contacts/contact.html')

def product_contact(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        salesmen_email = request.POST['salesmen_email']
        
        product = get_object_or_404(Product, pk=product_id)
        
        #is_paid=request.POST.get('is_paid', False)
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Product_Contact.objects.all().filter(product=product, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this product !")
                return redirect('/products/'+product_id)
        product_contact = Product_Contact(product=product, name=name, email=email, phone=phone, message=message, user_id=user_id)
        product_contact.save()
        
        # Send Email
        send_mail(
            'Product Inquiry',
            f'There has been an inquiry for {product.no}. Sign into the admin panel for more info.',
            'nwcn0307@gmail.com',# admin email
            [salesmen_email], #to email
            fail_silently=False
        )
        messages.success(request, "Your request has been submitted, a direct sale will get back to you soon !")
    return redirect('/products/'+product_id)
    #return render(request, 'contacts/contact.html')

def takeOrder(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        name = request.POST['name']
        price = int(request.POST['price'])
        onOrderQty = int(request.POST['onOrderQty'])
        #amount = int(request.POST['amount'])
        user_id = request.POST['user_id']
        salesmen_id = request.POST['salesmen_id']

        # Calculate the amount
        amount = price * onOrderQty
        
        product = get_object_or_404(Product, pk=product_id)
        # Check if the user already has this product in their cart
        if onOrderQty > product.stockQty:
            messages.error(request, "Quantity exceeds available stock.")
            return redirect('product', product_id=product_id)

        existing_order = TakeOrder.objects.filter(product=product, user_id=user_id).first()
        if existing_order:
            existing_order.onOrderQty += onOrderQty
            existing_order.amount = existing_order.price * existing_order.onOrderQty  # Update amount
            existing_order.save()
        else:
            # Create a new order
            takeOrder = TakeOrder(product=product, price=price, onOrderQty=onOrderQty, amount=amount, name=name, user_id=user_id, salesmen_id=salesmen_id)
            takeOrder.save()


        messages.success(request, "This product has been added to your shopping cart!")
    return redirect('/products/' + product_id)
        
    #     if request.user.is_authenticated:
    #         #user_id = request.user.id
    #         has_contacted = TakeOrder.objects.all().filter(product=product, user_id=user_id)
    #         if has_contacted:
    #             messages.error(request, "You have already made an inquiry for this product at this time !")
    #             return redirect('/products/'+product_id)
    #     takeOrder = TakeOrder(product=product, price=price, onOrderQty=onOrderQty, name=name, user_id=user_id, salesmen_id=salesmen_id)
    #     takeOrder.save()

    #     messages.success(request, "This product has been added to your shopping cart!")
    # return redirect('/products/'+product_id)

# def inc_Qty(request):
#     onOrederQty += 1
#     return(request)
# def dec_Qty(request):
#     onOrederQty -= 1
#     return(request)

def delete_takeOrder(request, takeOrder_id):
    contact = get_object_or_404(TakeOrder, pk=takeOrder_id)
    contact.delete()
    return redirect('dashboard')

def delete_take(request, takeOrder_id):
    contact = get_object_or_404(TakeOrder, pk=takeOrder_id)
    contact.delete()
    return redirect('shoppingCart')