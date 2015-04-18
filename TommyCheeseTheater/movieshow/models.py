from django.db import models
from django.contrib.auth.models import User
class Order(models.Model):
    moviename=models.CharField(max_length=255)
    theatername=models.CharField(max_length=255)
    tickets=models.IntegerField()
    moneys=models.IntegerField()
    orderedtime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,null=True)

class Movie(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    detail = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=255, blank=True)
    money = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255, blank=True)
    number = models.IntegerField()
    theaters=models.ManyToManyField('Theater',through='MovieShip')
    class Meta:
        
        db_table = 'Movie'
    def __str__(self):
        return self.name




class CheeseUser(models.Model):
     name=models.CharField(max_length=255)
     email=models.EmailField(db_index=True,unique=True)
     password=models.CharField(max_length=20,db_index=True)
class Theater(models.Model):
     name=models.CharField(max_length=255)
     
     def __str__(self):
       return self.name


class MovieShip(models.Model):
     movie=models.ForeignKey(Movie)
     theater=models.ForeignKey(Theater)
     tickets=models.PositiveIntegerField()
