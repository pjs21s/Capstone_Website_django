# Generated by Django 2.1.7 on 2019-04-13 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190413_1620'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title',)},
        ),
    ]