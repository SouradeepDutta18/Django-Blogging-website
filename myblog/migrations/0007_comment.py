# Generated by Django 3.1 on 2020-09-21 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20200920_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('post_time', models.DateField(auto_now_add=True)),
                ('content', models.CharField(default='', max_length=10000)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.blog')),
            ],
        ),
    ]
