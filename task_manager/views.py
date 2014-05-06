from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _


def testing(request):
    print request.LANGUAGE_CODE
    output = _("Welcome to my site")
    return HttpResponse(output)


@login_required(redirect_field_name='', login_url='/login/')
def home(request):
    user = authenticate(username='root', password='temporal')
    if user:
        print "DENTRO"
    else:
        print "FUERA"
    return render(request, 'dashboard.html')
