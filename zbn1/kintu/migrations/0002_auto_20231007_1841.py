# Generated by Django 2.2.6 on 2023-10-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kintu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='receiver',
            field=models.ManyToManyField(related_name='receiver', to='kintu.Account'),
        ),
    ]