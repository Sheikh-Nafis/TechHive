from django.db import models

class Game(models.Model):
    g_img = models.ImageField(upload_to='./games/')
    g_title = models.CharField(max_length=100)
    g_description = models.CharField(max_length=500)

class Desktop(models.Model):
    img = models.ImageField(upload_to='./pc/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

class Laptop(models.Model):
    l_img = models.ImageField(upload_to='./lp/')
    l_title = models.CharField(max_length=100)
    l_description = models.CharField(max_length=500)
    l_price = models.IntegerField()

class Monitor(models.Model):
    img = models.ImageField(upload_to='./m/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

class Component(models.Model):
    img = models.ImageField(upload_to='./c/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

class Accessorie(models.Model):
    img = models.ImageField(upload_to='./a/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

class Gadget(models.Model):
    img = models.ImageField(upload_to='./g/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

# python manage.py shell
# from home.models import Game
# game = Game(g_img = 'sv.png', g_title = 'Stardew Valley', g_description = 'Buy Stardew Valley· 
# $14.99.')
# game.save()