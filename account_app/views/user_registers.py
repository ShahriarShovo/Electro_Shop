from django.shortcuts import render, redirect
from account_app.models.user_model import User
from account_app.models.drop_down import Countries, Cities


def user_register(request):
    country = Countries.objects.all()
    if request.method == 'POST':
        print('request  = ', request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = email.split('@')[0]
        print("username = ", username)
        gender = request.POST['gender']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        country = request.POST['country']
        city = request.POST['city']
        country = Countries.objects.get(id=country)
        city = Cities.objects.get(id=city)

        user = User.objects.create_user(first_name=first_name, last_name=last_name, gender_choosed=gender,
                                        country=country, city=city,
                                        email=email, username=username, password=password)
        user.role = User.CUSTOMER

        """ if user.gender_choosed[gender] == User.MALE:
            user.save(commit=False)
        elif user.gender_choosed[gender] == User.FEMALE:
            user.save(commit=False) """
        user.save()

        return redirect('user_register')

    else:
        context = {
            'country_list': country
        }
        return render(request, 'accounts/user_register.html', context=context)
