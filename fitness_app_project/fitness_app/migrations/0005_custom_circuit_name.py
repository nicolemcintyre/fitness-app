# Generated by Django 2.0.5 on 2018-08-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0004_auto_20180731_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_circuit',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
