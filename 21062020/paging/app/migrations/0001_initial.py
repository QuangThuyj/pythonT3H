# Generated by Django 3.0.7 on 2020-06-21 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentNo', models.CharField(max_length=30, unique=True)),
                ('studentName', models.CharField(max_length=100)),
            ],
        ),
    ]