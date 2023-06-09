from django.shortcuts import render
from django_filters.views import FilterView
from .filters import ProductFilter
from .models import Product
from django.core.paginator import Paginator
from .forms import ProductForm

# Create your views here.
def index(request):
    form=ProductForm()
    return render(request,'index.html',{'form':form})



class ProductList(FilterView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()
        paginator = Paginator(products, self.paginate_by)
        page = self.request.GET.get('page')
        context['products'] = paginator.get_page(page)
        return context