# Generated by Django 4.2.1 on 2023-06-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='g_img',
            field=models.ImageField(upload_to='./games/'),
        ),
    ]