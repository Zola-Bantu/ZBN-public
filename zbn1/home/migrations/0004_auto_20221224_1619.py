# Generated by Django 2.2.6 on 2022-12-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_group_member_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]