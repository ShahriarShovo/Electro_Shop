from django.db import models
# from account_app.database.my_user_manager import Base_User_Manager
from .my_user_manager import Base_User_Manager
from .drop_down import Countries, Cities


from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    CUSTOMER = 2

    MALE = 1
    FEMALE = 2

    ROLE_CHOOSED = ((ADMIN, 'admin'), (CUSTOMER, 'customer'),)
    GENDER_CHOOSED = ((MALE, 'male'), (FEMALE, 'female'))

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20, blank=True, unique=True, null=True)

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOOSED, blank=True, null=True)
    gender_choosed = models.PositiveSmallIntegerField(choices=GENDER_CHOOSED, blank=True, null=True)

    # requires fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    country = models.ForeignKey(Countries, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = Base_User_Manager()

    def __str__(self) -> str:
        return self.email

    def has_perm(self, perm, object=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
