
from django.urls import path
from account_app.views.user_registers import user_register
from account_app.views.city_depent_by_country import city_dependent_by_country_view

urlpatterns = [
  
    path('register/', user_register, name='user_register'),
    path('city_dependent_by_country_view/', city_dependent_by_country_view,
         name='city_dependent_by_country_view'),

   
]
