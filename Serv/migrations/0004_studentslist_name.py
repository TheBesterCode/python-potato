# Generated by Django 2.2.12 on 2020-05-08 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Serv', '0003_auto_20200508_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentslist',
            name='name',
            field=models.CharField(default='', max_length=16),
        ),
    ]
