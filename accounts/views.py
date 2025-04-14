from django.shortcuts import render

# Create your views here.
def register_login(request):
    # add code of register and login

    return render(request, 'accounts/register_login.html')