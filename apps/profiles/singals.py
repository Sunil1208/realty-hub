import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates the user's profile every time a new user is created
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Saves the user's profile every time the user is updated
    """
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
