# Generated by Django 4.2.5 on 2023-09-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='price1',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]