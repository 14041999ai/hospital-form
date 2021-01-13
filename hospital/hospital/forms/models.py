from django.db import models
from multiselectfield import MultiSelectField

from django.conf import settings
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.admin import UserAdmin
# Create your models here.
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


from datetime import date
class Form(models.Model):
    start_date    = models.DateField(default='',)
    arrival_time  =models.TimeField(default='',)
    departure_time  =models.TimeField(default='',)

    REPEAT  =(
        ( 'No','None'),
        ('DA','Daily'),
        ('We','Weekly')     )
    repeat  =models.CharField(max_length=100,choices=REPEAT ,default='')

   # choices = models.ManyToManyField( REPEAT)
    SELECT_SHIFT  =(('Morning Shift-5am to 9 am','Morning Shift-5am to 9 am '),)
    select_shift = models.CharField(max_length=100, choices= SELECT_SHIFT, default='')
    WEEKDAYS =((1,'Sunday'),(2,'Monday'),(3,'Tuesday'),(4,'wednesday'),(5,'thrusday'),(6,'friday'),(7,'satuday'))
    weekdays  =MultiSelectField(default='',

        choices=WEEKDAYS
    )


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True,)
    email = models.EmailField(_('email address'), unique=True)
    native_name = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=10)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)
