# Generated by Django 3.1.5 on 2021-01-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='med',
            name='side_effects',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='med',
            name='storage',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='med',
            name='uses',
            field=models.TextField(max_length=1000),
        ),
    ]
