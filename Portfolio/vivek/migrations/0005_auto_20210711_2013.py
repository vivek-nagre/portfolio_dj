# Generated by Django 3.1.7 on 2021-07-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivek', '0004_auto_20210711_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(max_length=30),
        ),
    ]