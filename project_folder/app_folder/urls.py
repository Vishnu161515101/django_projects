from django.urls import path,include
from . import views

urlpatterns = [
    path('vishnu',views.vishnu,name='vishnu'),
    path('vardhan',views.vardhan,name='vardhan'),
    path('insert_data',views.insert_data,name='insert_data'),
    path('homepage',views.homepage,name='homepage'),
    path('login_data',views.login_data,name='login_data'),
    path('your_view',views.your_view,name='your_view'),
    
]
