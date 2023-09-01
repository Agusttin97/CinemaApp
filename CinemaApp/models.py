from django.db import models

# Create your models here.

class User(models.Model):
    
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    email = models.EmailField(null=True)
    
    def __str__(self):
        return f'{self.name} - {self.surname}'
    
class Movie(models.Model):
    
    movie = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    release = models.DateField()
    #_format = models.CharField(max_length=10) #Formatos 2D, 3D, 4D, etc
    
    def __str__(self):
        return f'{self.movie}'
    
class Cinema(models.Model):
    
    name = models.CharField(max_length=30,)
    location = models.CharField(max_length=30)
    capacity = models.IntegerField()
    movie = models.ManyToManyField(Movie)
    
    def __str__(self):
        return f'{self.name}'
    
    
    
