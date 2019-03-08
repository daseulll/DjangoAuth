from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save 
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import models

class User(AbstractUser):  # auth앱 내 User모델에 대한 Proxy
    sex = models.CharField(
        max_length=1,
        choices=(
            ('f', 'female'),
            ('m', 'male'),
        ),
        verbose_name='성별')
        
    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website_url = models.URLField(blank=True)


def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']:
        user = kwargs['instance']
        Profile.objects.create(user=user)
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)