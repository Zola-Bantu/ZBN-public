# Generated by Django 2.2.28 on 2024-01-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muntu', '0009_auto_20231028_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='msg_type',
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mosebedisi',
            name='pkn',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
