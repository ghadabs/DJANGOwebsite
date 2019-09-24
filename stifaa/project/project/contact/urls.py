from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from newsletter_subscription.backend import ModelBackend
from newsletter_subscription.urls import newsletter_subscriptions_urlpatterns

urlpatterns =[
    path('', views.contact, name ='stifaa-contact'),
    path('success/', views.contact, name='success'),
    # path('successs/', views.newsletter_signup, name='successs'),
]


