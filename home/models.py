from django.db import models

class Game(models.Model):
    g_img = models.ImageField(upload_to='games')
    g_title = models.CharField(max_length=100)
    g_description = models.CharField(max_length=500)
    g_price = models.IntegerField
