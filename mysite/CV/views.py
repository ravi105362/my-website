from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.conf import settings


def index(request):
    return render(request, 'CV/index.html')
