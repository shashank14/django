from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.timesince import timesince
from django.urls import reverse
#from django.core.exceptions import ValidationError

from django.db.models.signals import pre_save, post_save

# Create your models here.

from .validators import validate_author_email

PUBLISH_CHOICES = [
('draft','Draft'),
('publish','Publish'),
('private','Private')
]

# def validate_author_email(value):
#     if '@'in value:
#         return value
#     else:
#         raise ValidationError('Invalid email format')
#


class PostModelQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)

    def getby_id(self,value):
        return self.filter(id=value)

    def getby_title(self,value):
        return self.filter(title__icontains=value)

class PostModelManager(models.Manager):

    def get_queryset(self):
        return PostModelQuerySet(self.model,using=self._db)

    def all(self,*args,**kwargs):
        qs = super(PostModelManager,self).all(*args,**kwargs)
        return qs

    # def all(self,*args,**kwargs):
    #     qs = super(PostModelManager,self).all(*args,**kwargs).filter(active=True)
    #     return qs

    def get_post_by_id(self,id):
        qs = super(PostModelManager,self).get(id=id)
        return qs

    def get_set(self):
        # qs self.get_queryset(active=False)
        # return qs
        pass


class PostModel(models.Model):

    title           = models.CharField(max_length=50,
                                        unique=True,
                                        error_messages={
                                        'unique':'title has to be unique'
                                        },
                                        # help_text='please enter title here'
                                        )
    slug            = models.SlugField(null=True,blank=True,unique=True)
    post            = models.TextField(max_length=500)
    content         = models.CharField(max_length=500,null=True,blank=True)
    publish         = models.CharField(max_length=100,default='draft',choices=PUBLISH_CHOICES)
    author_email    = models.CharField(max_length=100,validators=[validate_author_email],null=True,blank=True)
    active          = models.BooleanField(default=True)
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
    updated         = models.DateTimeField(auto_now=True)# when was this record last updated
    timestamp       = models.DateTimeField(auto_now_add=True) # when was this record added



    objects =  PostModelManager()


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def save(self,*args,**kwargs):
        # if not self.slug and self.title:
        #     self.slug = slugify(self.title)
        # print('Hello override')
        super(PostModel,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={"id":self.id})

    def __str__(self):
        return self.title

    @property
    def age(self):
        return str(timesince(self.timestamp))+ ' ' + 'ago'



def post_model_pre_save_receiver(sender, instance, *args, **kwargs):
        try:
            print('pre-save')
            if not instance.slug and instance.title:
                instance.slug = slugify(instance.title)
        except:
            pass


pre_save.connect(post_model_pre_save_receiver, sender=PostModel)



# def blog_post_model_post_save_receiver(sender,instance, created, *args,**kwargs):
#     if created:
#         print('created')

#post_save.connect(blog_post_model_post_save_receiver,sender=PostModel)
