from django.urls import path
from apps.views import *

urlpatterns = [
    path('', index_view, name='index_view'),
    path('create_product', create_product, name='create_product'),
    path('create_Person', create_Person, name='create_Person'),
    path('create_category', create_category, name='create_category'),
    path('faker_data', faker_data, name='faker_data'),
]


