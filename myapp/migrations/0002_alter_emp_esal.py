# Generated by Django 5.0.1 on 2024-02-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='esal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
