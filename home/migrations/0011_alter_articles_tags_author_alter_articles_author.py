# Generated by Django 4.0 on 2022-02-06 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0010_remove_articles_caption_3_remove_articles_image_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=models.CharField(default='Impala', max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_staff', models.BooleanField(default=False, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.author'),
        ),
    ]
