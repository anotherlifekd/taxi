# Generated by Django 3.0.3 on 2020-02-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi_ukraine', '0005_auto_20200219_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Cancel'), (1, 'New'), (2, 'In-processing'), (4, 'Completed')], default=1),
        ),
    ]
