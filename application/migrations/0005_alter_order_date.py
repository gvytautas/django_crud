# Generated by Django 4.1.4 on 2023-01-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_vehicle_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
