# Generated by Django 2.2.5 on 2020-04-05 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_lib', '0004_movieitem_full_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(default='No data')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_lib.MovieItem')),
            ],
        ),
    ]