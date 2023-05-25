
from django.urls import path
from account_app.views.user_registers import user_register

urlpatterns = [
  
    path('register/', user_register, name='user_register'),

   
]
