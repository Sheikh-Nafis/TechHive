# Generated by Django 4.2.1 on 2023-06-05 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_accessorie_id_alter_component_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessorie',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='component',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='desktop',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='gadget',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='game',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='laptop',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='monitor',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='phone',
            name='stock',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='tv',
            name='stock',
            field=models.IntegerField(default=10),
        ),
    ]
