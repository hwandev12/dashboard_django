from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import DashboardTopCards


@login_required(login_url="/login/")
def index(request):
    cards = DashboardTopCards.objects.all()
    context = {'segment': 'index', 'cards': cards}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     try:
#
#         load_template = request.path.split('/')[-1]
#
#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template
#
#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))
#
#     except template.TemplateDoesNotExist:
#
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))
#
#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))

# tables
def tables(request):
    return render(request, 'home/tables.html')


# virtual reality
def virtual_reality(request):
    return render(request, 'home/virtual-reality.html')


# RTL section
def rtl(request):
    return render(request, 'home/rtl.html')


# profiles section
def profiles(request):
    return render(request, 'home/profile.html')


@login_required(login_url="/login/")
def billing(request):
    return render(request, 'home/billing.html')
