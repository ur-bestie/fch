# Generated by Django 4.1.7 on 2023-09-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_walletfund_walletbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='wafund',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.DeleteModel(
            name='walletbalance',
        ),
    ]
