from django.shortcuts import render


def base_home(request):
    return render(request, 'base/pages/home.html')
