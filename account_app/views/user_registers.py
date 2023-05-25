from django.shortcuts import render



def user_register(request):
    return render(request, 'accounts/user_register.html')