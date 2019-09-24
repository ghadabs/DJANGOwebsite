from django.urls import path
from . import views


urlpatterns =[
    path('', views.sale_list, name ='sale_list'),
    path("<str:category>/", views.sale_category, name="sale_category"),
    path('<int:id>', views.sale_detail, name='sale_detail'),
    path("<subcategory>", views.sale_subcategory, name="sale_subcategory"),
   
]