from django.http.response import HttpResponseNotFound

__author__ = 'RSevilla'


def handle404():
    return HttpResponseNotFound()
