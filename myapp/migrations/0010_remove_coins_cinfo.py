# Generated by Django 4.1.7 on 2023-09-26 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_wafund_coins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coins',
            name='cinfo',
        ),
    ]