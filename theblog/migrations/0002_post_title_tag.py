# Generated by Django 4.2.2 on 2023-06-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blogger', max_length=255),
        ),
    ]
