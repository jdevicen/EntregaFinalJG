# Generated by Django 4.1 on 2022-10-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProyecto4', '0005_remove_server_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='imagen',
            field=models.ImageField(null=True, upload_to='servers'),
        ),
    ]
