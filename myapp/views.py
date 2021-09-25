from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from .models import Value
from .forms import Registration
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def main(request):
    marco = Value.objects.get(drinker = 'Marco')
    antor = Value.objects.get(drinker = 'Antor')
    return render(request, 'myapp/main.html', {'marco': marco, 'antor': antor})


def drinkmilo(request):
    marco = Value.objects.get(drinker = 'Marco')
    marco.drinks_num += 1
    marco.add_date = timezone.now()
    marco.save()
    return redirect('main')

def reset(request):
    marco = Value.objects.get(drinker = 'Marco')
    marco.drinks_num = 0
    marco.save()
    return redirect('main')

def drinkmilo2(request):
    antor = Value.objects.get(drinker = 'Antor')
    antor.drinks_num += 1
    antor.add_date = timezone.now()
    antor.save()
    return redirect('main')

def reset2(request):
    antor = Value.objects.get(drinker = 'Antor')
    antor.drinks_num = 0
    antor.save()
    return redirect('main')

def registration(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Registration successful')
            return redirect('main')
        messages.error(request, 'Fail. Invalid info')
        return render(request, 'myapp/registration.html', {'form':form})

    else:
        form = Registration()
    return render(request, 'myapp/registration.html', {'form': form})


# Create your views here.
