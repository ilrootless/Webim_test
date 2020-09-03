from django.urls import path

from .views import *

app_name='auth_vk'
urlpatterns = [
    # Выход
    path('accounts/logout/', VKLogoutView.as_view(), name='logout'),
    # Главная
    path('', index, name='index')
]