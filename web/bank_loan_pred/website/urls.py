from django.contrib import admin
from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('special/', views.special, name='special'),
    path('contact/<int:test>', views.contact, name='contact'),
    path('api_pred/', views.api_predict, name='api_predict'),
    #path('api_data/', views.api_data, name='api_data'),
]