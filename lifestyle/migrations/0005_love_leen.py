# Generated by Django 4.0 on 2022-04-15 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifestyle', '0004_alter_gallery_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='love',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='leen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lifestyle.love')),
            ],
        ),
    ]
