# Generated by Django 4.0.4 on 2022-05-26 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Screenshot',
            field=models.CharField(max_length=150),
        ),
    ]
