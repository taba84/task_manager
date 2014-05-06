from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render


def login(request):
    return HttpResponse("Hello")
    return render(request, 'index.html')


@login_required(redirect_field_name='', login_url='/login/')
def home(request):
    user = authenticate(username='root', password='temporal')
    if user:
        print "DENTRO"
    else:
        print "FUERA"
    return render(request, 'home.html')
