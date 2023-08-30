from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index, name='home'),
    path('about/',about, name='about'),
    path('booking/',booking, name='booking'),
    path('doctors/',contact, name='contact'),
    path('contact/',doctors, name='doctors'),
    path('department/',department, name='department'),





]