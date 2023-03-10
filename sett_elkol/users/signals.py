import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from config.settings.base import AUTH_USER_MODEL
from sett_elkol.chef.models import Chef
from sett_elkol.customer.models import Customer
from sett_elkol.users.models import User

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_customer_chef(sender, instance, created, **kwargs):
    if created and instance.user_type == User.UserType.CUSTOMER:
        Customer.objects.create(
            user=instance,
            country=instance.country,
            city=instance.city,
            gender=instance.gender,
            )
    if created and instance.user_type == User.UserType.CHEF:
        Chef.objects.create(user=instance,
                            country=instance.country,
                            city=instance.city, 
                            gender=instance.gender,
                            )

@receiver(post_save, sender=AUTH_USER_MODEL)
def save_customer_chef(sender, instance, **kwargs):
    if  instance.user_type == User.UserType.CUSTOMER:
        instance.customer.save()
        logger.info(f"{instance}'s customer created")
    if  instance.user_type == User.UserType.CHEF:
        instance.chef.save()
        logger.info(f"{instance}'s chef created")
