from django.shortcuts import render
from contact.models import Contact
# Create your views here.
def contact(request):
    contacts = Contact.objects.order_by('contact_id')
    context = {'contacts' : contacts}
    return render(request, 'contact/contact.html', context)

def contact_detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    context = {'contact' : contact}
    return render(request, 'contact/contactdetail.html', context)