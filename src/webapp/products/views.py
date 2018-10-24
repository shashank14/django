from django.shortcuts import render
from django.views.generic import ListView

from .models import Product
# Create your views here.


def product_list_view(request):

    queryset = Product.objects.all()
    context = {'object_list':queryset}
    template_name = 'products/products.html'
    return render (request,template_name,context)

def product_detail_view(request,id=None):
    qs = Product.objects.get(id=id)
    context = {'product':qs}
    template_name = 'products/productdetail.html'
    return render (request,template_name,context)

def about_view(request):
    template_name = 'products/about.html'
    context={}
    return render (request,template_name,context)

def contact_view(request):
    template_name = 'products/contact.html'
    context={}
    return render (request,template_name,context)

def register_view(request):
    template_name = 'products/register.html'
    context={}
    return render (request,template_name,context)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/products.html'



# from django.shortcuts import render
#  from django.views.generic import ListView
#  from testapp.models import Book
#
#  # Create your views here.
#  class BookListView(ListView):
#  model=Book
#  template_name='testapp/books.html'
#  context_object_name='list_of_books'
#  #default tempalte: book_list.html
#  #default context object: book_list
