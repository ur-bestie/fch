# Generated by Django 4.1.7 on 2023-10-11 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_ucoins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ethereum',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trc20',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tron',
            name='user',
        ),
        migrations.RemoveField(
            model_name='xlm',
            name='user',
        ),
        migrations.RemoveField(
            model_name='xrp',
            name='user',
        ),
        migrations.DeleteModel(
            name='bitcoin',
        ),
        migrations.DeleteModel(
            name='ethereum',
        ),
        migrations.DeleteModel(
            name='trc20',
        ),
        migrations.DeleteModel(
            name='tron',
        ),
        migrations.DeleteModel(
            name='xlm',
        ),
        migrations.DeleteModel(
            name='Xrp',
        ),
    ]
