# Generated by Django 2.2 on 2019-05-08 20:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0008_auto_20190508_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
