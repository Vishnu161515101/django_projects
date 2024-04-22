from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def vishnu(request):
    return HttpResponse('hello vishnu')

def vardhan(request):
    template = loader.get_template('entry_page.html')
    return HttpResponse(template.render())