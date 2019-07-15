from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

	
	
#def contacts_connect(request):
#    context = locals()
#    template = 'contact.html'
#    return render(request, template, context)

def vc_portal(request):
    context = locals()
    template = 'vc_portal.html'
    return render(request, template, context)

def vc_learn(request):
    context = locals()
    template = 'vc_learn.html'
    return render(request, template, context)

def st_hub(request):
    context = locals()
    template = 'st_hub.html'
    return render(request, template, context)

def st_connect(request):
    context = locals()
    template = 'st_connect.html'
    return render(request, template, context)

def careers(request):
    context = locals()
    template = 'careers.html'
    return render(request, template, context)

def library(request):
    context = locals()
    template = 'library.html'
    return render(request, template, context)	