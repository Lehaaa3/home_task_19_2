# Generated by Django 4.2.6 on 2023-11-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_version_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='is_active',
            field=models.BooleanField(verbose_name='активная версия'),
        ),
    ]
