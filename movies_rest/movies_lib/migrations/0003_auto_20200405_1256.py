# Generated by Django 2.2.5 on 2020-04-05 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies_lib', '0002_auto_20200405_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieitem',
            old_name='author',
            new_name='director',
        ),
    ]