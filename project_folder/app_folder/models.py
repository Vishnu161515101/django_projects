from django.db import models

# Create your models here.
class dajngo_project(models.Model):
    name_for_user=models.CharField(max_length=500)
    email_for_user=models.CharField(max_length=500)
    password_for_user=models.CharField(max_length=500)
