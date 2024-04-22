from django.urls import path,include
from . import views

urlpatterns = [
    path('vishnu',views.vishnu,name='vishnu'),
    path('vardhan',views.vardhan,name='vardhan'),
    path('insert_data',views.insert_data,name='insert_data'),
    
]
