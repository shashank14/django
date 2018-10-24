from django.contrib import admin
from .models import PostModel
# Register your models here.

# title           = models.CharField(max_length=50,
#                                     unique=True,
#                                     error_messages={
#                                     'unique':'title has to be unique'
#                                     },
#                                     help_text='please enter title here'
#                                     )
# slug            = models.SlugField(editable=False,null=True,blank=True,unique=True)
# post            = models.CharField(max_length=100)
# content         = models.CharField(max_length=500,null=True,blank=True)
# publish         = models.CharField(max_length=100,default='draft',choices=PUBLISH_CHOICES)
# author_email    = models.CharField(max_length=100,validators=[validate_author_email],null=True,blank=True)
# active          = models.BooleanField(default=True)
# view_count      = models.IntegerField(default=0)
# publish_date    = models.DateField(auto_now=False,auto_now_add=False,default=timezone.now)
# updated         = models.DateTimeField(auto_now=True)# when was this record last updated
# timestamp       = models.DateTimeField(auto_now_add=True)

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','active']
    fields = ['title','slug','post','content','publish','author_email',
    'active','view_count','publish_date','updated','timestamp','new_content','get_age']

    readonly_fields=['updated','timestamp','new_content','get_age']

    def new_content(self,obj,*args,**kwargs):
        return obj.title

    def get_age(self,obj,*args,**kwargs):
        return obj.age

    class Meta:
        model = PostModel

admin.site.register(PostModel,PostModelAdmin)
