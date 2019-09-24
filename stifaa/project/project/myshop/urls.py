from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("<str:category>/", views.product_category, name="product_category"),
    path('<int:id>', views.product_detail, name='product_detail'),    
    path("<subcategory>", views.product_subcategory, name="product_subcategory"),
]
0