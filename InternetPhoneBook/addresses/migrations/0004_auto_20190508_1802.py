# Generated by Django 2.2 on 2019-05-08 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_addressperson'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AddressPerson',
        ),
        migrations.RemoveField(
            model_name='address',
            name='name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='second_name',
        ),
    ]
