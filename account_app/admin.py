from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account_app.models.user_model import User
from account_app.models.user_profile import UserProfile
from account_app.models.drop_down import Countries, Cities
# Register your models here.

class Custom_User_Admin(UserAdmin):
    list_display=('email', 'first_name','last_name','username',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()


""" class Custom_user_Profile(UserAdmin):
    list_display=('email', 'first_name','last_name','username',) """



admin.site.register(User,Custom_User_Admin)

admin.site.register(UserProfile)
admin.site.register(Countries)
admin.site.register(Cities)

