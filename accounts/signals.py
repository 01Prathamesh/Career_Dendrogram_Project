# Updated Code
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new UserProfile for the new user
        UserProfile.objects.create(user=instance)
    else:
        # Update the existing UserProfile if it exists
        try:
            user_profile = UserProfile.objects.get(user=instance)
            user_profile.save()
        except UserProfile.DoesNotExist:
            # Handle the case where the UserProfile does not exist (if necessary)
            pass
