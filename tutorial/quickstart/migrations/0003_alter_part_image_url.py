# Generated by Django 3.2.7 on 2021-10-25 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_part_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='Image_Url',
            field=models.ImageField(max_length=200, null=True, upload_to='image'),
        ),
    ]
