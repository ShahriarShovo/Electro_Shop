# Generated by Django 4.2.1 on 2023-05-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender_choosed',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'male'), (2, 'female')], null=True),
        ),
    ]