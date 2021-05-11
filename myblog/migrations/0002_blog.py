# Generated by Django 3.1 on 2020-09-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('author_name', models.CharField(default='', max_length=30)),
                ('content', models.CharField(default='', max_length=5000)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
                ('video_id', models.CharField(default='', max_length=50)),
            ],
        ),
    ]