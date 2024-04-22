from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def vishnu(request):
    return HttpResponse('hello vishnu')

def vardhan(request):
    template = loader.get_template('entry_page.html')
    return HttpResponse(template.render())


def insert_data(request):
    name_for_user=request.POST['user_name']
    email_for_user=request.POST['Emails']
    password_for_user=request.POST['Password_use']
    return HttpResponse(name_for_user+email_for_user+password_for_user)