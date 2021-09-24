from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .models import Value

def main(request):
    marco = Value.objects.get(drinker = 'Marco')
    antor = Value.objects.get(drinker = 'Antor')
    return render(request, 'myapp/main.html', {'marco': marco, 'antor': antor})


def drinkmilo(request):
    marco = Value.objects.get(drinker = 'Marco')
    marco.drinks_num += 1
    marco.add_date = timezone.now()
    marco.save()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def reset(request):
    marco = Value.objects.get(drinker = 'Marco')
    marco.drinks_num = 0
    marco.save()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def drinkmilo2(request):
    antor = Value.objects.get(drinker = 'Antor')
    antor.drinks_num += 1
    antor.add_date = timezone.now()
    antor.save()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")

def reset2(request):
    antor = Value.objects.get(drinker = 'Antor')
    antor.drinks_num = 0
    antor.save()
    return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")



# Create your views here.
