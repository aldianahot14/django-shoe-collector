# Generated by Django 5.0.1 on 2024-02-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_shoeaccessory'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoeaccessory',
            name='shoes',
            field=models.ManyToManyField(to='main_app.shoe'),
        ),
    ]