# Generated by Django 2.2 on 2019-05-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0009_auto_20190508_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
