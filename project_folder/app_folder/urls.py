from django.urls import path,include
from . import views

urlpatterns = [
    path('vishnu',views.vishnu,name='vishnu'),
    path('vardhan',views.vardhan,name='vardhan'),
    path('vardhan1/', views.vardhan1, name='vardhan1'),
    path('insert_data',views.insert_data,name='insert_data'),
    path('homepage',views.homepage,name='homepage'),
    path('login_data',views.login_data,name='login_data'),
    path('your_view',views.your_view,name='your_view'),
    path('your_post_view',views.your_post_view,name='your_post_view'),
    path('your_destination_view',views.your_destination_view,name='your_destination_view'),
    
]
