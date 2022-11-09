from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from .models import *
from django.core.mail import send_mail


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_user(created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Transaction)
def post_save_balance(instance: Transaction, **kwargs ):
    user = Profile.objects.get(id=instance.user.id)
    user.balance += instance.sum
    user.save()

# SENT MAIL
# @receiver(post_save, sender=Transaction)
# def sent(instance: Transaction, **kwargs ):
#     user = Profile.objects.get(id=instance.user.id)
#     send_mail(f"{user.balance}", 'helloalohamatuta', '542avy3@gmail.com', ["542avy3@gmail.com"])
