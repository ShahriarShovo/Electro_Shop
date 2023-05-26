from django.shortcuts import render, redirect
from account_app.models.user_model import User



def user_register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        gender=request.POST['gender']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        user= User.objects.create_user(first_name=first_name, last_name=last_name,
                                       email=email,username=username,password=password)
        user.role=User.CUSTOMER

        """ if user.gender_choosed[gender] == User.MALE:
            user.save(commit=False)
        elif user.gender_choosed[gender] == User.FEMALE:
            user.save(commit=False) """
        user.save()
            
        return redirect('user_register')
    
    else:

        return render(request, 'accounts/user_register.html')