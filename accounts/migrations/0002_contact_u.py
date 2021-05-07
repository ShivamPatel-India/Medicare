# Generated by Django 3.1.5 on 2021-04-11 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_u',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('messeage', models.TextField(max_length=900)),
                ('name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]