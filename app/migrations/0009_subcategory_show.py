# Generated by Django 3.1.1 on 2021-03-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210327_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
