from django.shortcuts import render
import utilities

def index(request):
    c = utilities.friends(request.user)
    return render(request, 'auth_vk/index.html', context={'a': c})
