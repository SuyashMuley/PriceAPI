# Generated by Django 3.2 on 2021-06-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='compare_price',
            field=models.FloatField(default=0),
        ),
    ]
