# Generated by Django 3.2 on 2021-05-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_person_info_date_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_info',
            name='Date_Found',
            field=models.DateField(),
        ),
    ]