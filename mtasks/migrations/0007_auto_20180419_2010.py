# Generated by Django 2.0.2 on 2018-04-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtasks', '0006_auto_20180418_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='resolution',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='resolution and feedback'),
        ),
    ]
