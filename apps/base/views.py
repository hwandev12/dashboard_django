from django.shortcuts import render
from .models import *


def base_home(request):
    sliders = HomeSliders.objects.all()
    fashion_cards = FashionCards.objects.all()
    phone_cover = PhoneBackCovers.objects.all()
    context = {
        "sliders": sliders,
        "fashion_cards": fashion_cards,
        "phone_cover": phone_cover
    }
    return render(request, 'base/pages/home.html', context)
