# Generated by Django 3.1.1 on 2021-03-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210327_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincaraousalad',
            name='FirstLine',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='maincaraousalad',
            name='SecondLine',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]