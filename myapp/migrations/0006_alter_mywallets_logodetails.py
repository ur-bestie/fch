# Generated by Django 4.1.7 on 2023-09-26 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_mywallets_logodetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywallets',
            name='logodetails',
            field=models.TextField(max_length=2000),
        ),
    ]
