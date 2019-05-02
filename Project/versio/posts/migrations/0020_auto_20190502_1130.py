# Generated by Django 2.1.7 on 2019-05-02 11:30

from django.db import migrations, models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20190426_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
