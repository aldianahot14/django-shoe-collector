# Generated by Django 5.0.1 on 2024-02-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_shoeaccessory_shoes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoeaccessory',
            name='shoes',
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoeAccessory',
            field=models.ManyToManyField(to='main_app.shoeaccessory'),
        ),
    ]