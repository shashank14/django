from django.conf.urls import url,include
from .views import (product_list_view,ProductListView,product_detail_view,
about_view,contact_view,register_view)


urlpatterns = [
    url(r'^$',product_list_view,name='home'),
    url(r'^home$',product_list_view,name='home'),
    url(r'^about$',about_view,name='about'),
    url(r'^contact$',contact_view,name='contact'),
    #url(r'^login$',login,name='login'),
    url(r'^register$',register_view,name='register'),
    url(r'^(?P<id>\d+)/$',product_detail_view,name='detail'),
    #url(r'^cbv/$',ProductListView.as_view()),
]
