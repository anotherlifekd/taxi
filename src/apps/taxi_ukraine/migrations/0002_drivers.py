# Generated by Django 3.0.3 on 2020-02-19 06:23

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('taxi_ukraine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_free', models.BooleanField(default=True)),
                ('license_plate_number', models.ForeignKey(db_column='taxi_ukraine_cars', on_delete=django.db.models.deletion.PROTECT, to='taxi_ukraine.Cars')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
