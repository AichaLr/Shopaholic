# Generated by Django 2.0.13 on 2019-04-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_auto_20190416_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='UPC',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
