# Generated by Django 3.2.25 on 2024-03-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financiacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financiacion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]