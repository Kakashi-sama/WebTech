# Generated by Django 2.1.7 on 2019-04-22 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_account_cr_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='cr_number',
        ),
    ]
