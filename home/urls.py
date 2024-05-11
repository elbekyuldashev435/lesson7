from django.urls import path
from .views import home_page, GetTest

app_name = 'home'
urlpatterns = [
    path('', home_page, name='home_page'),
    path('test/', GetTest.as_view(), name='test')
]