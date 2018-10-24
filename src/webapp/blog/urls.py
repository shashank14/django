from django.conf.urls import url
from .views import create_blog, update_blog, post_model_list, blog_detail



urlpatterns = [
url(r'^listblogs/$',post_model_list,name='list'),
url(r'^detailblog/(?P<id>\d+)/$',blog_detail,name='detail'),
url(r'^createblog/$',create_blog,name='create'),
url(r'^updateblog/(?P<id>\d+)/$',update_blog,name='update'),
]
