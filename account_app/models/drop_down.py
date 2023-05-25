from django.db import models
from tools.models import InitModels


class Countries(InitModels):
    countries_name=models.CharField(max_length=30, unique=True, blank=True,null=True)
    def __str__(self):
        return self.countries_name
    
    
class Cities(InitModels):
    contries=models.ForeignKey(Countries, on_delete=models.CASCADE)
    city_name=models.CharField(max_length=30, unique=True, blank=True,null=True)

    def __str__(self):
        return self.city_name

    
