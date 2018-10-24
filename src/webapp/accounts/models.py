from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse

from django.db.models.signals import post_save

from .utils import code_generator

class MyUserManager(BaseUserManager):


    def create_user(self, username, email, first_name, last_name, date_of_birth, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            first_name,
            last_name,
            date_of_birth=date_of_birth,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


USERNAME_REGEX = '^[a-zA-X]*$'


class MyUser(AbstractBaseUser):

    username = models.CharField(max_length=125,
                                validators=[RegexValidator(regex=USERNAME_REGEX,
                                            message='first name must be alphabetic',
                                            code='Invalid user')
                                            ],
                                 unique=True,
                                )

    first_name = models.CharField(max_length=125,
                                validators=[RegexValidator(regex=USERNAME_REGEX,
                                            message='first name must be alphabetic',
                                            code='Invalid first name')
                                            ],
                                )

    last_name = models.CharField(max_length=125,
                                validators=[RegexValidator(regex=USERNAME_REGEX,
                                            message='last name must be alphabetic',
                                            code='Invalid last name')
                                            ],
                                )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(auto_now=False,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name','date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return str(self.first_name + ' ' + slef.last_name)

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        #Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # def get_absolute_url(self):
        #return "{id}/".format(id=self.id)
        #return reverse("accounts:logout")
        # pass


    # def get_url(self):
    #     #return "{id}/".format(id=self.id)
    #     return reverse("accouts:home")




class Profile(models.Model):

    user     = models.OneToOneField(settings.AUTH_USER_MODEL)
    city     = models.CharField(max_length=25,null=True, blank=True)
    country  = models.CharField(max_length=25,null=True, blank=True)


    def __str__(self):
        return str(self.user.username)

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            ActivationProfile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)



class ActivationProfile(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL)
    key     = models.CharField(max_length=120)
    expired = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.key = code_generator()
        super(ActivationProfile, self).save(*args, **kwargs)


def post_save_activation_receiver(sender, instance, created, *args, **kwargs):
    if created:
        #send email
        #url = http://127.0.0.0:9090/activate/ + instance.key
        print('activation created')

post_save.connect(post_save_activation_receiver, sender=ActivationProfile)
