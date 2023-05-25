from django.contrib import admin
from account_app.models.user_model import User
from account_app.models.user_profile import UserProfile
from account_app.models.drop_down import Countries, Cities
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Countries)
admin.site.register(Cities)

