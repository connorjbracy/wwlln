# Generated by Django 4.0.2 on 2022-05-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCFrontEnd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pipeline',
            field=models.TextField(null=True),
        ),
    ]