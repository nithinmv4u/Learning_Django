from django.shortcuts import render, redirect
from django. http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.views.decorators.cache import never_cache
from django.contrib.auth import logout


# Create your views here.

def signup(request):
    # form from forms.py
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfuly')
            return redirect('login')

    messages.error(request, 'Please try again with a different username and password')
    return render(request, 'app/signup.html', {'form' : form})

def login(request):
    if 'username' in request.session:
         return render(request, 'home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect('home')
            if user.is_superuser:
                return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    return render(request, 'app/login.html')

@never_cache
def home(request):
    context = {
            'users': User.objects.all()
        }
    if 'username' in request.session:
        return render(request,'app/index.html', context)
    else:
        return redirect('login')

def about(request):
    if 'username' in request.session:
        return render(request, 'app/about.html')
    else:
        return redirect('login')





def logout(request):
    if 'username' in request.session:
        request.session.flush()

    return redirect('login')

def test(request):

    context={
        'test' : 'test11'
    }
    return render(request, 'app/test.html', context)


