# Generated by Django 2.0.2 on 2018-04-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='feedback',
            field=models.CharField(blank=True, max_length=2000, verbose_name='feedback'),
        ),
    ]
