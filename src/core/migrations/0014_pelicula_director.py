# Generated by Django 5.1.7 on 2025-04-06 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_director_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.director'),
        ),
    ]
