from django.shortcuts import redirect,render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def home(request):
    firstname=request.session.get('firstname')
    # if request.method=="POST":
    #     return HttpResponse(f"year is {year} and month is {month}")
        # firstname=request.POST['firstname']
        #return render(request,'userlog/index.html',{'firstname':firstname})
    return render(request,'userlog/index.html',{'firstname':firstname})

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

    return render(request,'userlog/signup.html')
    # return HttpResponse('hello')   

def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        # firstname=request.POST['firstname']

        user=authenticate(username=username,password=password)
        if user is not None:
            request.session["username"]=username #session creation
            firstname=user.first_name
            request.session["firstname"]=firstname
            login(request,user)
            messages.success(request,"Logged in succesfully")
            # firstname=user.first_name
            # context={'firstname':firstname}
            # return render(request,"userlog/index.html",{'firstname':firstname})
            return redirect('home')
            # return HttpResponseRedirect(reverse(request,"userlog/index.html",context))
        else:
            messages.error(request,"Bad Credentials")
            return redirect('signin')
    return render(request,'userlog/signin.html')

def signout(request):
    if 'username' in request.session:
        request.session.flush() #session clear
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('home')

# def new(request,firstname=""):
    # return HttpResponse(f"<h1>Hello {{firstname}}")