from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.user_model import User
from .models.user_profile import UserProfile

@receiver(post_save,sender=User)

def create_profile_signals(sender,instance,created,**kwargs):

    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:
            UserProfile.objects.create(user=instance)
            
