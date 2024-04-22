from django.urls import path,include
from . import views

urlpatterns = [
    path('vishnu',views.vishnu,name='vishnu'),
    path('vardhan',views.vardhan,name='vardhan'),
    
]
