# Generated by Django 4.0 on 2022-05-04 06:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0010_delete_dietplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='dietplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5000)),
                ('des', tinymce.models.HTMLField()),
            ],
            options={
                'db_table': 'dietplan',
            },
        ),
    ]
