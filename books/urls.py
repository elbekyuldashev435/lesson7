from django.urls import path
from .views import *


app_name = 'books'
urlpatterns = [
    path('test/', ListView.as_view(), name='book-list')

]