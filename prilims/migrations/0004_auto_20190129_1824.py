# Generated by Django 2.1.5 on 2019-01-29 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prilims', '0003_auto_20190129_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='College_name',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='email',
        ),
        migrations.RemoveField(
            model_name='scorecard',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]