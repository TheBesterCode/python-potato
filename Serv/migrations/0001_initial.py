# Generated by Django 2.2.12 on 2020-05-08 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Serv.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Serv.StudentsList'),
        ),
    ]