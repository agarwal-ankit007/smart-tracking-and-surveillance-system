# Generated by Django 3.2 on 2021-05-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_person_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_info',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
