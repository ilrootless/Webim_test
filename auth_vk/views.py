from django.shortcuts import render

def index(request):
    return render(request, 'auth_vk/index.html')
