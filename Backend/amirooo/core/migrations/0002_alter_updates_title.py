# Generated by Django 4.2.4 on 2023-11-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
