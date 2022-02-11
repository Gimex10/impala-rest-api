# Generated by Django 4.0 on 2022-02-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_product_options_product_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('-user',)},
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='author',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='phone',
        ),
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads/'),
        ),
    ]
