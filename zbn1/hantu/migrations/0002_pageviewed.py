# Generated by Django 2.2.28 on 2024-05-25 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hantu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageViewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(max_length=50)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('country_code', models.CharField(blank=True, max_length=10, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('region_code', models.CharField(blank=True, max_length=10, null=True)),
                ('town', models.CharField(blank=True, max_length=50, null=True)),
                ('lat', models.FloatField(blank=True, max_length=50, null=True)),
                ('lon', models.FloatField(blank=True, max_length=50, null=True)),
                ('timezone', models.CharField(blank=True, max_length=20, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=10, null=True)),
                ('isp', models.CharField(blank=True, max_length=50, null=True)),
                ('organization', models.CharField(blank=True, max_length=50, null=True)),
                ('az', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Page viewed',
                'verbose_name_plural': 'Pages viewed',
                'ordering': ['-timestamp'],
            },
        ),
    ]
