# Generated by Django 2.1.5 on 2019-01-28 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quesion', models.TextField(max_length=500)),
                ('choice1', models.TextField(max_length=100)),
                ('choice2', models.TextField(max_length=100)),
                ('choice3', models.TextField(max_length=100)),
                ('choice4', models.TextField(max_length=100)),
                ('correct_answer', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
