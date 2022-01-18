from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Account(models.Model):

    Publicity = (
                    ('Instagram', 'Instagram'),
                    ('Facebook', 'Facebook'),
                    ('Whatsapp', 'Whatsapp'),
                    ('LinkedIn', 'LinkedIn'),
                    ('College', 'College'),
                    ('Others', 'Others')
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

    Mobile_Number                   = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Whatsapp_Number                 = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    Organisation                    = models.CharField(max_length=200, blank=True, null=True)
    Publicity                       = models.CharField(choices=Publicity, max_length=50, blank=True, null=True)
    

    def _str_(self):
        return self.user