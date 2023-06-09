from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')

def signup(request):
    if request.method=="POST":
        # username=request.POST.get('username')
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confpassword=request.POST['confpassword']

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"Your account has been created succesfully..!")

        return redirect('signin')

    return render(request,'authentication/signup.html')
    # return HttpResponse('hello')   

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            firstname=user.first_name
            return render(request,"authentication/index.html",{'firstname':firstname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request,'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('home')