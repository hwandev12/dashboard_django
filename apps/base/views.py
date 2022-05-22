from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import *
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
    template_name = 'base/../templates/registration/signup.html'
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


# create login view here
class LoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(LoginView, self).form_valid(form)
