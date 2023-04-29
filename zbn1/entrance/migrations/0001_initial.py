# Generated by Django 2.2.28 on 2023-04-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('path', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]