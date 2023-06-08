from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    g_img = models.ImageField(upload_to='./games/')
    g_title = models.CharField(max_length=100)
    g_description = models.CharField(max_length=500)
    stock = models.IntegerField(default=10)

class Game2(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./games/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    stock = models.IntegerField(default=10)

class Game3(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./games/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    stock = models.IntegerField(default=10)

class Desktop(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./pc/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Desktop1(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./pc/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Laptop(models.Model):
    id = models.AutoField(primary_key=True)
    l_img = models.ImageField(upload_to='./lp/')
    l_title = models.CharField(max_length=100)
    l_description = models.CharField(max_length=500)
    l_price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Laptop2(models.Model):
    id = models.AutoField(primary_key=True)
    l_img = models.ImageField(upload_to='./lp/')
    l_title = models.CharField(max_length=100)
    l_description = models.CharField(max_length=500)
    l_price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Monitor(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./m/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Monitor2(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./m/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Component(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./c/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Accessorie(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./a/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)


class Gadget(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./g/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Gadget2(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./g/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Tv(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./t/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./p/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

class Console(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='./p/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stock = models.IntegerField(default=10)

# python manage.py shell
# from home.models import Game
# game = Game(g_img = 'sv.png', g_title = 'Stardew Valley', g_description = 'Buy Stardew Valley· 
# $14.99.')
# game.save()