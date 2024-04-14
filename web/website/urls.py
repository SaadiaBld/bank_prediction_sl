from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('predict/', views.predict, name='predict'),
    #path('api_data/', views.api_data, name='api_data'),
    #path('contact/<int:test>', views.contact, name='contact'),
]