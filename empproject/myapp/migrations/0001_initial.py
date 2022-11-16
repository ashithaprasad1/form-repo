# Generated by Django 4.1.1 on 2022-09-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('edoj', models.DateField()),
                ('edesig', models.CharField(max_length=50)),
                ('eexp', models.FloatField()),
                ('ecompany', models.CharField(max_length=50)),
                ('esal', models.IntegerField()),
            ],
        ),
    ]
