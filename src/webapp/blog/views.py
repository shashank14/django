from django.shortcuts import render
from django.contrib import messages


# Create your views here.

from .forms import PostModelForm
from .models import PostModel


def create_blog(request):
    form = PostModelForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        obj = form.save()
        print(obj.title)
        msg = obj.title + ' created successfully !!'
        messages.success(request,msg)
        form = PostModelForm()
        context = {'form':form}

    template_name  = 'blog/createblog.html'
    return render (request,template_name,context)



def update_blog(request,id):
    qs = PostModel.objects.get(id=id)
    form = PostModelForm(request.POST or None,instance=qs)
    context = {'form':form}
    if form.is_valid():
        print(form.cleaned_data.get('title'))
        obj = form.save()
        #print(obj.title)
        msg = obj.title + ' updated successfully !!'
        messages.success(request,msg)
        #form = PostModelForm()
        #context = {'form':form}

    template_name  = 'blog/createblog.html'
    return render (request,template_name,context)



def post_model_list(request):
    query = request.GET.get('q')
    #print(query)
    qs = PostModel.objects.all()
    if query is not None:
        qs = qs.filter(title__icontains=query)
    context = { 'object_list': qs }
    template_name = 'blog/listblogs.html'
    return render (request,template_name,context)


def blog_detail(request,id):
    qs = PostModel.objects.get(id=id)
    context = {'object':qs}
    template_name  = 'blog/blogdetail.html'
    return render (request,template_name,context)

















# from django.shortcuts import render,redirect
#  from testapp.models import Employee
#  from testapp.forms import EmployeeForm
#
#
#  # Create your views here.
#  def retrieve_view(request):
#  employees=Employee.objects.all()
#  return render(request,'testapp/index.html',{'employees':employees})
#
#  def create_view(request):
#  form=EmployeeForm()
#  if request.method=='POST':
#  form=EmployeeForm(request.POST)
#  if form.is_valid():
#  form.save()
#  return redirect('/')
#  return render(request,'testapp/create.html',{'form':form})
#




 #  import os
 # os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudfbvproject.settings')
 # import django
 # django.setup()
 #
 # from testapp.models import *
 # from faker import Faker
 # from random import *
 # faker=Faker()
 # def populate(n):
 # for i in range(n):
 # feno=randint(1001,9999)
 # fename=faker.name()
 # fesal=randint(10000,20000)
 # feaddr=faker.city()
 # emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
 # populate(20)

  # deletion
# A: from django.db import models
#
#  # Create your models here.
#  class Employee(models.Model):
#  eno=models.IntegerField()
#  ename=models.CharField(max_length=64)
#  esal=models.FloatField()
#  eaddr=models.CharField(max_length=256
