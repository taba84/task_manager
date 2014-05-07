from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext as _
from task_manager.forms import LoginForm
from users.models import Profile


def testing(request):
    print request.LANGUAGE_CODE
    output = _("Welcome to my site")
    return HttpResponse(output)


def home(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=request.POST["username"], password=request.POST["password"])
                if user:
                    auth.login(request, user)
                    profile = Profile(user=user, last_login_source=request.META["REMOTE_ADDR"])
                    profile.save()
                    return render(request, 'dashboard.html')
        return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')