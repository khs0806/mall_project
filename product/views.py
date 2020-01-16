from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from rest_framework import generics
from rest_framework import mixins

from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
from .serializers import ProductSerializer
from fcuser.decorators import admin_required, login_required

# Create your views here.

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(login_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
                    name=form.data.get('name'),
                    price=123456789,
                    description=form.data.get('description'),
                    stock=1
                )
        product.save()
        return super().form_valid(form)

class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context

def edit(request, post_id):
    product = get_object_or_404(Product, pk=post_id)
    print(request.method)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=product)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = RegisterForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product':product})    
