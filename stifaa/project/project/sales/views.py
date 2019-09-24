from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category ,Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
# ,Subcategory

def sale_list(request,category_slug=None):
    category = None
    subcategory = None
    categories = Category.objects.all()
    # subcategories=Subcategory.objects.all()
    products=Product.objects.all()
    paginator = Paginator(products, 12) 
    page = request.GET.get('page') # < Get the page number
    products = paginator.get_page(page)
    return render(request, 'sales.html', {   'category':category,
                                             'categories': categories,
                                             'products': products})

def sale_subcategory(request,subcategory): 
    print("tetaaaaada")
    if request.method=='GET':
        sub = request.GET.get('subcategory')
        products = Product.objects.filter(subcategory=subcategory)
        # products = Product.objects.filter(product.subcategory = sub).order_by('-created')
        paginator = Paginator(products, 12) 
        page = request.GET.get('page') # < Get the page number
        products = paginator.get_page(page)
        categories = Category.objects.all()
        print("tetaaaaada")
        context = {
            "categories": categories,
            "products": products }
        return render(request, "sales_subcategory.html", context)
def sale_category(request, category):
    products = Product.objects.filter(
        category__name__contains=category
    ).order_by(
        '-created'
    )

    paginator = Paginator(products, 12) 
    page = request.GET.get('page') # < Get the page number
    products = paginator.get_page(page)
    categories = Category.objects.all()
    # print("tetaaaaada")
    context = {
        "category": category,
        "products": products,
        "categories":categories
    }
    return render(request, "sales_category.html", context)
    


def sale_detail(request,id):
    
    product=Product.objects.get(id=id)
    products= Product.objects.filter(category=product.category).order_by('-created')[0:4]
    return render(request,'sales_detail.html',{'product': product,
                                         'products': products})
