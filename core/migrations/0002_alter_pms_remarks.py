# Generated by Django 4.0.6 on 2022-07-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pms',
            name='remarks',
            field=models.TextField(null=True),
        ),
    ]