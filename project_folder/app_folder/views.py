from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
@csrf_protect

# Create your views here.

def vishnu(request):
    return HttpResponse('hello vishnu')

def vardhan(request):
    template = loader.get_template('entry_page.html')
    return HttpResponse(template.render())


def insert_data(request):
    if request.method == 'POST':
        # Check if the request method is POST before accessing POST data
        name_for_user = request.POST.get('user_name', '')  # Use .get() to avoid KeyError
        email_for_user = request.POST.get('Emails', '')    # Use .get() to avoid KeyError
        password_for_user = request.POST.get('Password_use', '')  # Use .get() to avoid KeyError
        # Do something with the form data, such as saving it to a database
        return HttpResponse(name_for_user + email_for_user + password_for_user)
    else:
        # Handle other HTTP methods (GET, etc.) if needed
        return HttpResponse("This view expects POST requests only.")
