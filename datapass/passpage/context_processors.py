from .import views
from django.http import HttpResponse
from .forms import MyForm
from .models import MyModel

# BELOW CODE WAS USED TO PASS CONTEXT TO 'mypage.html' BEFORE SAVING TO DATABASE
def my_context_processor(request):
    return {'my_form_data': request.POST.dict()}

# #USING DATA FROM DATABASE
# def my_context_processor_b(request):
#     my_data=MyModel.objects.all()
#     return {'my_data':my_data}