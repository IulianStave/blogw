# Create a user profile for each new user
# Add a signal that saves a profile when a new user is created
# User is the sender that creates the profile when saved

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# if that user was created create a Profile object with user being the instance of the user that was created
# the receiver is the create_profile function 
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
   instance.profile.save()

