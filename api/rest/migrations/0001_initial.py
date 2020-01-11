# Generated by Django 3.0.2 on 2020-01-11 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_coding', models.DateField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('timezone', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['date_coding'],
            },
        ),
    ]
