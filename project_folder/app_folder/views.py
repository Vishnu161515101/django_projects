from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_folder.models import dajngo_project
from django.views.decorators.csrf import csrf_protect
@csrf_protect



# Create your views here.

def vishnu(request):
    return HttpResponse('hello vishnu')

def vardhan(request):
    template = loader.get_template('entry_page.html')
    return HttpResponse(template.render())


def insert_data(request):
    name_for_user1=request.POST['user_name']
    email_for_user1=request.POST['Emails']
    password_for_user1=request.POST['Password_use']
    c1=dajngo_project.objects.create(name_for_user=name_for_user1,email_for_user=email_for_user1,password_for_user=password_for_user1)
    c1.save()
    return HttpResponse('its done')