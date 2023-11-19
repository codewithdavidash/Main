from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import ApplicationModel
from django.contrib import messages
from .forms import (
    SignupForm,
    AppForm
)


@login_required
def contact(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            onSave = form.save(commit=False)
            onSave.user = request.user
            onSave.save()
            messages.success(
                request, f'Your Application was successfully sent!')
            return redirect('index')
    else:
        form = AppForm()
    return render(request, 'core/contact.html', {
        'form': form
    })


@login_required
def admin(request):
    form = ApplicationModel.objects.all()
    return render(request, 'core/admin.html', {
        'form': form
    })


def index(request):
    return render(request, 'core/index.html', {})


def services(request):
    return render(request, 'core/services.html', {})


def products(request):
    return render(request, 'core/products.html', {})


def about(request):
    return render(request, 'core/about.html', {})


def aims(request):
    return render(request, 'core/aims.html', {})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account was successfully!')
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/"
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")