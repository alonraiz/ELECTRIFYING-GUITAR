from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from manager import manager

x = manager()

def index(request):
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def fire(request):
    x.onFails()
    return HttpResponse("")
