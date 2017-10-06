

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings

def index(request):
    return render(request, 'personal/home.html')