# Generated by Django 3.2.6 on 2021-09-08 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='megusta_users',
        ),
    ]
