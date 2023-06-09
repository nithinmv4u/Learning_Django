from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from app.forms import CreateUserForm
from django.views.decorators.cache import never_cache


# Create your views here.
def admin(request):
    context = {}
    return render(request, 'customAdmin/adminpanel.html', context)

def adminLogin(request):
    if 'username' in request.session:
        return redirect('dashboard')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password=password)

        if user is not None:
            login(request,user)
            request.session['username'] = username
            if user.is_superuser:
                return redirect('dashboard')
            else:
                messages.info(request, 'Access Denied, You don\'t have admin privilages')
        else:
            messages.info(request, 'Username or password is Incorrect')
    return render(request, 'customAdmin/login.html', context)

@never_cache
@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    if 'username' in request.session:
        context = {
            'users': User.objects.all()
        }
        return render(request, 'customAdmin/dashboard.html', context)
    else:
        return redirect('admin_login')

@user_passes_test(lambda u: u.is_superuser)
def searchUser(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        user = User.objects.filter(username__icontains = searched)
        context={
        'searched' : searched,
         'user' : user,
        }
        return render(request, 'customAdmin/searchUser.html', context)
    else:
        return render(request, 'customAdmin/searchUser.html')

@user_passes_test(lambda u: u.is_superuser)
def createUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('dashboard')
    return render(request, 'customAdmin/createUser.html', {'form' : form, 'title': 'Submit'})

@user_passes_test(lambda u: u.is_superuser)
def updateUser(request,id):
    user=User.objects.get(pk=id)
    form = CreateUserForm(instance = user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Details Updated Successfully')
            return redirect('dashboard')
    return render(request, 'customAdmin/createUser.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def deleteUser(request, id):
    user=User.objects.get(pk=id)
    if request.method == 'POST':
        if user.is_superuser:
            pass
        else:
            user.delete()
        return redirect('dashboard')
    context = { 'user': user}
    return render(request, 'customAdmin/deletePage.html', context)

@user_passes_test(lambda u: u.is_superuser)
def adminLogout(request):
    logout(request)
    if 'username' in request.session:
        request.session.flush()
    return redirect('admin_login')








