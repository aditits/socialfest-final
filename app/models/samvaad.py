from django.conf import settings
from django.db import models


class Samvaad(models.Model):

    Participant                         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.Participant