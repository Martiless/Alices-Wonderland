from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    The user profile model will be used
    to maintain shipping information and
    order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    users_phone = models.CharField(max_length=20, null=True, blank=True)
    users_country = CountryField(blank_label='Country *',  max_length=200, null=True, blank=True)
    users_postcode = models.CharField(max_length=20, null=True, blank=True)
    users_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    users_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    users_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    users_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Will create or update the
    users profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
