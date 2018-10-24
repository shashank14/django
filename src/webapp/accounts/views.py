from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import UserLoginForm

def login_view(request):
    form = UserLoginForm(request.POST or None)
    template_name = 'accounts/login.html'
    context = {'form': form}
    #print(request.user.is_authenticated())
    if form.is_valid():
        username = form.cleaned_data.get('user')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/products/')
        else:
            print('error')

        form = UserLoginForm()

    return render(request,template_name,context)

def signup_view(request):

    template_name = 'accounts/register.html'
    context = {}
    return render(request,template_name,context)

#@login_required(login_url='/login/')

@login_required
def settings_view(request):

    template_name = 'accounts/usersettings.html'
    context = {}
    return render(request,template_name,context)


def logout_view(request):
    template_name = 'accounts/logout.html'
    logout(request)
    return render(request,template_name,{})




# print(form.cleaned_data.get('user'))
# print(form.cleaned_data.get('password'))
# print(form.cleaned_data)
