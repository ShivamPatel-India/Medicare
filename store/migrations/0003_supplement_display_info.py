# Generated by Django 3.1.5 on 2021-02-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_delete_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplement',
            name='display_info',
            field=models.TextField(default='', max_length=200),
        ),
    ]
