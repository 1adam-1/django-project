# Generated by Django 5.0.3 on 2024-05-01 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catastrophe',
            name='nom',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
