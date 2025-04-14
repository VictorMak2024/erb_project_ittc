from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Activity_Contact, Course_Contact, Product_Contact
from activities.models import Activity
from courses.models import Course
from products.models import Product
from django.core.mail import send_mail

# Create your views here.
def activity_contact(request):
    if request.method == 'POST':
        activity_id = request.POST['activity_id']
        activity = request.POST['activity']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        salesmen_email = request.POST['salesmen_email']
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Activity_Contact.objects.all().filter(activity_id=activity_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already applied sitting for this activity !")
                return redirect('/activities/'+activity_id)
        activity_contact = Activity_Contact(activity=activity, activity_id=activity_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        activity_contact.save()
        
        activitys = Activity.objects.get(id=activity_id)
        if activitys.onenquiry_sit == activitys.total_sit:
            messages.error(request, "Course is full",
            )
            return redirect('/activitys/'+activity_id)
        elif activitys.price != 0:
            messages.warning(request, "You need to pay $"+str(activitys.price)+" for this activity to enroll. Once payment is done, you can proceed to enroll in this activity !")
        else:
            activitys.onenquiry_sit = activitys.onenquiry_sit +1
            activitys.save()
        # Send Email
        send_mail(
            'Activity Inquiry',
            'There has been an inquiry for '+activity+'. Sign into the admin panel for more info.',
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
        course = request.POST['course']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        salesmen_email = request.POST['salesmen_email']
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Course_Contact.objects.all().filter(course_id= course_id , user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already applied for this course !")
                return redirect('/courses/'+course_id)
        course_contact = Course_Contact(course=course, course_id=course_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        course_contact.save()

        courses = Course.objects.get(id=course_id)
        if courses.onenquiry_sit == courses.total_sit:
            messages.error(request,                "Course is full",
            )
            return redirect('/courses/'+course_id)
        elif courses.price != 0:
            messages.warning(request, "You need to pay $"+str(courses.price)+" for this course to enroll. Once payment is done, you can proceed to enroll in this course !")
        else:
            courses.onenquiry_sit = courses.onenquiry_sit +1
            courses.save()


        
        # Send Email
        send_mail(
            'Course Inquiry',
            'There has been an inquiry for '+course+'. Sign into the admin panel for more info.',
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
        product = request.POST['product']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        salesmen_email = request.POST['salesmen_email']
        if request.user.is_authenticated:
            #user_id = request.user.id
            has_contacted = Product_Contact.objects.all().filter(product_id=product_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing !")
                return redirect('/products/'+product_id)
        product_contact = Product_Contact(product=product, product_id=product_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        product_contact.save()
        # products = Product.objects.get(id=product_id)
        # products.onenquiry_sit = products.onenquiry_sit +1
        # products.save()

        # Send Email
        send_mail(
            'Product Inquiry',
            'There has been an inquiry for '+product+'. Sign into the admin panel for more info.',
            'nwcn0307@gmail.com',# admin email
            [salesmen_email], #to email
            fail_silently=False
        )
        messages.success(request, "Your request has been submitted, a direct sale will get back to you soon !")
    return redirect('/products/'+product_id)
    #return render(request, 'contacts/contact.html')



# def delete_contact(request, contact_id):
#     contact = get_object_or_404(Product_Contact, pk=contact_id)
#     contact.delete()
#     return redirect('dashboard')