# Generated by Django 4.1.7 on 2023-10-13 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_backuptransaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backuptransaction',
            old_name='cname',
            new_name='name',
        ),
    ]
