# Generated by Django 5.0 on 2023-12-19 03:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_userprofile_otp_userprofile_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('first_name', models.CharField(default=None, max_length=30)),
                ('last_name', models.CharField(default=None, max_length=30)),
                ('password', models.CharField(default=None, max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.player'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]