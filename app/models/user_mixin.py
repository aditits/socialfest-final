from django.db import models

from .account import Account


class UserMixin(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    details = models.ForeignKey(Account, on_delete=models.CASCADE, db_index=True, blank=True, null=True)

    class Meta:
        abstract = True
