# Generated by Django 4.0 on 2021-12-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='headline',
            field=models.CharField(max_length=250),
        ),
    ]
