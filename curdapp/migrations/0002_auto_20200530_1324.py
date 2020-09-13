# Generated by Django 3.0.6 on 2020-05-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('name', models.CharField(max_length=60)),
                ('salary', models.FloatField()),
                ('adress', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
