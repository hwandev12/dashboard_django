from django.contrib import messages
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from . import models
from .forms import *
from .models import *


# base home function here
def base_home(request):
    sliders = HomeSliders.objects.all()
    fashion_cards = FashionCards.objects.all()
    phone_cover = PhoneBackCovers.objects.all()
    phone_accessories = PhoneAccessories.objects.all()
    context = {
        "sliders": sliders,
        "fashion_cards": fashion_cards,
        "phone_cover": phone_cover,
        "phone_accessories": phone_accessories
    }
    return render(request, 'base/pages/home.html', context)


# create sign up view
class SignupView(CreateView):
    template_name = 'base/registration/signup.html'
    initial = {'key': 'value'}
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})

