from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Activity_Contact, Course_Contact, Product_Contact
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
    # add code of dashboard
    activity_contacts = Activity_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    course_contacts = Course_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    product_contacts = Product_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {'activity_contacts' : activity_contacts, 'course_contacts' : course_contacts, 'product_contacts' : product_contacts}

    return render(request, 'accounts/dashboard.html' , context)