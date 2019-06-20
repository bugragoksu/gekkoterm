from django.db import models

# Create your models here.
class User(models.Model):

    username=models.CharField(max_length=50,verbose_name="username")
    password=models.CharField(max_length=50,verbose_name="password")
    nameSurname=models.CharField(max_length=255,verbose_name="nameSurname")
    email=models.CharField(max_length=255,verbose_name="email")

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

    def __str__(self):
        return self.username

    
