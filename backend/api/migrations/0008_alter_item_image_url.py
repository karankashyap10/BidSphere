# Generated by Django 5.1.7 on 2025-04-19 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_image_item_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_url',
            field=models.ImageField(default='item_default.jpg', null=True, upload_to='item_images'),
        ),
    ]
