from django.shortcuts import render
import utilities


def index(request):
    if request.user.is_authenticated:
        friends = utilities.friends(request.user)
        return render(request, 'auth_vk/index.html', context={'friends': friends})
    else:
        return render(request, 'auth_vk/index.html')
