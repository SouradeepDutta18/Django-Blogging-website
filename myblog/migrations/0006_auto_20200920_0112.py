# Generated by Django 3.1 on 2020-09-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20200919_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_title',
            field=models.CharField(default='', max_length=70),
        ),
    ]
