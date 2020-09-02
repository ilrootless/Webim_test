from django.urls import path

from .views import index

app_name='auth_vk'
urlpatterns = [
    path('', index, name='index')
]