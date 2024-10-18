from django.urls import path
from .views import criar_cliente

app_name = 'users'

urlpatterns = [
    path('register/', criar_cliente, name='register_user'),
]