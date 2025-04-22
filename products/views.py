from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def products(request, category_title = None):
    # if category_title:
    #     categories = get_object_or_404(Category, title = category_title)
    #     products = Product.objects.filter(category=categories).order_by('no')
    # else:
    #     categories = Category.objects.all()
    #     products = Product.objects.all()

    # paginator = Paginator(products, 3)
    # page = request.GET.get('page')
    # paged_products = paginator.get_page(page)
    
    # context = {'products' : paged_products , 'categories' : categories}
    
    if category_title:
        category = get_object_or_404(Category, title=category_title)
        products = Product.objects.filter(title=category).order_by('no')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        context = {'products': paged_products, 'category': category}
    
    else:
        categories = Category.objects.all()
        products = Product.objects.all()

        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)

        context = {'products': paged_products, 'categories': categories}
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.stockQty = product.stockQty - product.onOrderQty
    context = {'product' : product}
    return render(request, 'products/product.html', context)

def search(request):
    return render(request, 'products/search.html')
