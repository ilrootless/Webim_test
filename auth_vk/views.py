from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
import utilities

# Главная страница
def index(request):
    if request.user.is_authenticated:
        friends = utilities.friends(request.user)
        return render(request, 'auth_vk/index.html', context={'friends': friends})
    else:
        return render(request, 'auth_vk/index.html')

# Выход
class VKLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'auth_vk/index.html'
