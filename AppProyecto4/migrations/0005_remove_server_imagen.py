# Generated by Django 4.1 on 2022-10-19 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto4', '0004_server_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='imagen',
        ),
    ]
