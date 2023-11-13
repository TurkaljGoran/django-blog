from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



@receiver(post_save, sender=User)
def create_profile(sender: User, instance: User, created: bool, **kwargs):
    """
    - this is a receiver function
    - args 'sender', 'instance', 'created' and **kwargs are sent to the function by post_save signal
    - check if created is true, then create a profile for the user after the user is created
    """
    
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender: User, instance: User,  **kwargs):

    instance.profile.save()