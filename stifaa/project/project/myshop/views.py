from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 12) 
    page = request.GET.get('page') # < Get the page number
    products = paginator.get_page(page)
    return render(request, 'products.html', {'category': category,
                                             'categories': categories,
                                             # 'subcategories': subcategories,
                                             'products': products})


def product_subcategory(request,subcategory): 
    print("tetaaaaada")
    if request.method=='GET':
        # sub = request.GET.get('subcategory')
        products = Product.objects.filter(subcategory=subcategory)
        paginator = Paginator(products, 12) 
        page = request.GET.get('page') # < Get the page number
        products = paginator.get_page(page)
        # products = Product.objects.filter(product.subcategory = sub).order_by('-created')
        categories = Category.objects.all()
        print("tetaaaaada")
        context = {
            
            "categories": categories,
            "products": products }
        return render(request, "subcategory.html", context)

def product_category(request, category):
    products = Product.objects.filter(
        category__name__contains=category
    ).order_by('-created')
    paginator = Paginator(products, 12) 
    page = request.GET.get('page') # < Get the page number
    products = paginator.get_page(page)
    categories = Category.objects.all()
    # print("tetaaaaada")
    context = {
        "category": category,
        "products": products,
        "categories": categories
    }

    return render(request, "category.html", context)


def product_detail(request, id):
    print("tekhdem")
    product = Product.objects.get(id=id)
    products = Product.objects.filter(
        category=product.category).order_by('-created')[0:4]
    return render(request, 'detail.html', {'product': product,
                                           'products': products})
