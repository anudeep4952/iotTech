# Generated by Django 2.1.7 on 2019-03-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part1', '0003_auto_20190324_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(blank=True, default='sss', max_length=255),
        ),
    ]
