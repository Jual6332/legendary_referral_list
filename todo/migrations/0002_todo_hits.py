# Generated by Django 2.2.3 on 2019-07-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]