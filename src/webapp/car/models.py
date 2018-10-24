from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL


class Car(models.Model):

    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)



    def __str__(self):
        return self.name
