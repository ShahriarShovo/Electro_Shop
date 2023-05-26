from django.db import models

#from account_app.database.user_model import User
from .user_model import User

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    profile_picture=models.ImageField(upload_to='user/profile_picture',blank=True,null=True)
    cover_photo=models.ImageField(upload_to='user/cover_picture',blank=True,null=True)
    address=models.CharField(max_length=500,blank=True,null=True)
    country=models.CharField(max_length=50, blank=True,null=True)
    state=models.CharField(max_length=50, blank=True,null=True)
    city=models.CharField(max_length=50, blank=True,null=True)
    pin_code=models.CharField(max_length=10, blank=True,null=True)
    latitude=models.CharField(max_length=50, blank=True,null=True)
    longitute=models.CharField(max_length=50, blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modify_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email