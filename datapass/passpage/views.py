from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template.context import RequestContext
from .forms import MyForm
from .models import MyModel

# Create your views here.
def home(request):
    form=MyForm()
    return render(request,'passpage/index.html',{'form':form})

def data(request):
    my_data=MyModel.objects.all()
    return render(request,'passpage/data.html',{'my_data':my_data})

def mypage(request):
    if request.method=='POST':
        form = MyForm(request.POST)
        if form.is_valid():
            my_field_data = form.cleaned_data['my_field']
            my_num_data=form.cleaned_data['my_num']
            new_model = MyModel(my_field=my_field_data,my_num=my_num_data)
            new_model.save()
        # return redirect('mypage')
    else:
        form=MyForm()
        # return render(request,'passpage/mypage.html',{ 'form' : form })
    # uname=request.session.get('uname')

    #here context passing is not working since already saved data from 'contexrocessor.py' is
    # being taken at 'mypage.html' through jinja templating 
    return render(request,'passpage/mypage.html',{'form':form})