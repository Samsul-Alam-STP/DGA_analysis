from django.urls import path
from .views import *

app_name = 'dga_result'

urlpatterns = [
    path('', form_view, name='form_view'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),

]
