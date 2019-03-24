# Generated by Django 2.1.5 on 2019-03-23 22:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20190321_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='posts',
            name='posts_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]