from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.http import HttpResponseRedirect #to redirect to the constructed URL
from django.template import loader
# from django.urls import reverse #to get the URL pattern name
from app_folder.models import dajngo_project
from .models import dajngo_project 
from django.views.decorators.csrf import csrf_protect
@csrf_protect



# Create your views here.

def vishnu(request):
    return HttpResponse('hello vishnu')

def vardhan(request):
    # Fetch the value of the 'message' query parameter
    message = request.session.get('message', None)
    # return HttpResponse(message)
    # Now you can use the 'message' variable in your view logic
    if message == '12':
        del request.session['message']
        message = 'Please enter correct email / password!'
        context = {'message': message}
        template = loader.get_template('entry_page.html')
        return HttpResponse(template.render(context, request))
    elif message == '13':
        del request.session['message']
        message = 'Alredy this mail existed'
        context = {'message': message}
        template = loader.get_template('entry_page.html')
        return HttpResponse(template.render(context, request))
    
    else:
         template = loader.get_template('entry_page.html')
         return HttpResponse(template.render())
    
def vardhan1(request):
    # Fetch the value of the 'message' query parameter
    message = request.session.get('message', None)

  
    
    # Now you can use the 'message' variable in your view logic
    if message:
        message = 'Please enter correct email / password!'
        context = {'message': message}
        template = loader.get_template('entry_page.html')
        return HttpResponse(template.render(context, request))
    else:
         template = loader.get_template('entry_page.html')
         return HttpResponse(template.render())
    


def insert_data(request):
        name_for_user1=request.POST['user_name']
        email_for_user1=request.POST['Emails']
        password_for_user1=request.POST['Password_use']
        user = dajngo_project.objects.filter(name_for_user=name_for_user1,email_for_user=email_for_user1).first()
        if user:
             message = '13'
             request.session['message'] = message
             return redirect('/vardhan') 
        else:
            c1=dajngo_project.objects.create(name_for_user=name_for_user1,email_for_user=email_for_user1,password_for_user=password_for_user1)
            c1.save()
            return redirect('/vardhan')

def login_data(request):
    name_for_user1 = request.POST.get('user_name')
    password_for_user1 = request.POST.get('Password_use')

    user = dajngo_project.objects.filter(name_for_user=name_for_user1, password_for_user=password_for_user1).first()
    
    if user:
        return redirect('/homepage')
    else:
        # message = '1'
        # return redirect('vardhan?message={}'.format(message))
       message = '12'
       request.session['message'] = message
       return redirect('/vardhan')
    

def homepage(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())




def your_view(request):
    message = 'Please enter correct email / password!'
    context = {'message': message}
    template = loader.get_template('test_html.html')
    return HttpResponse(template.render(context, request))


def your_post_view(request):
    if request.method == 'POST':
        # Process the POST data
        message = '12'

        # Store the message in the session
        request.session['message'] = message

        # Redirect to another view
        return redirect('your_destination_view')
    else:
        # Handle other HTTP methods
        pass


def your_destination_view(request):
    # Retrieve the message from the session
    message = request.session.get('message', None)

    if message:
        # Clear the message from the session after retrieving it
        del request.session['message']

        # Process the message or do something with it
        return HttpResponse(message)
    else:
        # Handle the case where message is not found
        return HttpResponse("Message not found")