# Generated by Django 4.2.1 on 2023-06-08 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_cpu_cpu1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cpu',
        ),
        migrations.DeleteModel(
            name='Cpu1',
        ),
    ]
