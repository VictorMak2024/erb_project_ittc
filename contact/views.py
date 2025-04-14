from django.shortcuts import render
from contact.models import Contact
# Create your views here.
def contact(request):
    contacts = Contact.objects.order_by('contact_id')
    context = {'contacts' : contacts}
    return render(request, 'contact/contact.html', context)