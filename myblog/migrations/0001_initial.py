# Generated by Django 3.1 on 2020-09-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='querypost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=25)),
                ('name', models.CharField(default='', max_length=35)),
                ('contact_no', models.CharField(default='', max_length=11)),
                ('query', models.TextField(default='')),
            ],
        ),
    ]
