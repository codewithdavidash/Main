# Generated by Django 4.2.6 on 2023-10-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='date_of_birth',
            field=models.CharField(max_length=50),
        ),
    ]
