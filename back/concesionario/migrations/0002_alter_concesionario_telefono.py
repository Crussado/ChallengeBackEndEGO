# Generated by Django 3.2.25 on 2024-03-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concesionario',
            name='telefono',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
