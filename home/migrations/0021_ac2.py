# Generated by Django 4.2.1 on 2023-06-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_delete_accessorie2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ac2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='./a/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField(default=10)),
            ],
        ),
    ]
