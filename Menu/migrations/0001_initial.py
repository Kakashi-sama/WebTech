# Generated by Django 2.1.7 on 2019-04-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=120)),
            ],
        ),
    ]