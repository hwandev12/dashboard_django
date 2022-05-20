from django.shortcuts import render

from .models import HomeSliders


def base_home(request):
    sliders = HomeSliders.objects.all()
    context = {
        "sliders": sliders
    }
    return render(request, 'base/pages/home.html', context)
