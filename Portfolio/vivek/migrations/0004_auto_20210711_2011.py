# Generated by Django 3.1.7 on 2021-07-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivek', '0003_auto_20210711_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(blank=True, default=''),
        ),
    ]
