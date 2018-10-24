from django.db import models
import random
from django.urls import reverse

# Create your models here.


class Product(models.Model):

    title               = models.CharField(max_length=50)
    description         = models.TextField()
    price               = models.DecimalField(decimal_places=2,max_digits=19,default=39.99)
    image               = models.ImageField(upload_to='products',null=True,blank=True)
    image_two           = models.ImageField(upload_to='products',null=True,blank=True)

    #image               = models.FileField(upload_to='products/',null=True,blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return "{id}/".format(id=self.id)
        return reverse("products:detail",kwargs={"id":self.id})

    def get_url(self):
        #return "{id}/".format(id=self.id)
        return reverse("products:home")
