# Generated by Django 3.2.25 on 2024-03-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_alter_modelo_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='parte',
            name='url_img',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
