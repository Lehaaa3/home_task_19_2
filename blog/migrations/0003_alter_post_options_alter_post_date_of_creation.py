# Generated by Django 4.2.6 on 2023-10-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_of_creation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('date_of_creation',), 'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
