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
# python manage.py shell
# from home.models import Game
# game = Game(g_img = 'sv.png', g_title = 'Stardew Valley', g_description = 'Buy Stardew Valley· 
# $14.99.')
# game.save()