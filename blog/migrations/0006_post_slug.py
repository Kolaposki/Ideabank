# Generated by Django 3.0.3 on 2020-03-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_auto_20200325_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
