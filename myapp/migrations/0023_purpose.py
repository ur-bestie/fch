# Generated by Django 4.1.7 on 2023-10-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_bitcoin_user_ethereum_user_trc20_user_tron_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pur/%y')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=3000)),
            ],
        ),
    ]