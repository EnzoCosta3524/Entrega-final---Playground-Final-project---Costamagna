# Generated by Django 5.1.7 on 2025-04-06 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.PositiveSmallIntegerField(max_length=50)),
                ('pais_de_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.pais')),
            ],
        ),
    ]
