# Generated by Django 2.2.28 on 2024-05-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muntu', '0010_auto_20240120_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='pke',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='pkn',
            field=models.CharField(default='0', max_length=5000),
        ),
    ]
