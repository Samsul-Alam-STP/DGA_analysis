from django.urls import path
from .views import *

urlpatterns = [
    path('', form_view, name='form_view'),
    path('data/', data_view, name='data_view'),
]
