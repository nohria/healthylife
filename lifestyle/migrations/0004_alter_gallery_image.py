# Generated by Django 4.0 on 2022-04-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0003_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]