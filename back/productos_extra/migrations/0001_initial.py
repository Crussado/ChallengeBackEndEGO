# Generated by Django 3.2.25 on 2024-03-08 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=16)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True)),
                ('tipo', models.BooleanField(choices=[(True, 'Servicio'), (False, 'Accesorio')])),
            ],
        ),
    ]
