from django.shortcuts import  redirect,get_object_or_404,render
from django.contrib import messages
from .models import Contactmessage
from datetime import datetime
# Create your views here.
def contactmessage(request):
  if request.method == 'POST':
        center = request.POST['contact_center']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        post_date = datetime.now()  # Set apply_date to the current date and time
        message = request.POST['message']    
        contact_id = request.POST['contact_id']   
        # Check if user has made inquiry already
        if request.user.is_authenticated:
            has_applied = Contactmessage.objects.all().filter(center=center, email=email)
            

        contactmessage = Contactmessage(
            center=center,
            post_date=post_date,
            # date_available=date_available,
            name=name,
            email=email,
            phone=phone,
            user_id=user_id,
            message=message
        )

        contactmessage.save()


        # Send success message
        messages.success(request, 'Your Inquiry has been submitted, our staff will get back to you soon')
        return redirect('/contactus/' + contact_id)