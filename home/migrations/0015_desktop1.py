# Generated by Django 4.2.1 on 2023-06-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_delete_cpu_delete_cpu1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='./pc/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField(default=10)),
            ],
        ),
    ]