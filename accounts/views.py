from django.shortcuts import render
from contacts.models import Activity_Contact, Course_Contact, Product_Contact

# Create your views here.
def register_login(request):
    # add code of register and login

    return render(request, 'accounts/register_login.html')

def dashboard(request):
    activity_contacts = Activity_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    course_contacts = Course_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    product_contacts = Product_Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {'activity_contacts' : activity_contacts, 'course_contacts' : course_contacts, 'product_contacts' : product_contacts}

    return render(request, 'accounts/dashboard.html' , context)
