from django.urls import path
from .views import RegisterView, LoginView
from home.views import home_page


app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('back/', home_page, name='home_page')
]