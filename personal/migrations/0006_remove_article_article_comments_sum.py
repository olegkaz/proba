# Generated by Django 2.1 on 2018-09-02 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20180902_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_comments_sum',
        ),
    ]
