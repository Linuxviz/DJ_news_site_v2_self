# Generated by Django 3.1.5 on 2021-01-25 12:23

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210123_0126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newstags',
            old_name='color',
            new_name='background_color',
        ),
        migrations.AddField(
            model_name='newstags',
            name='text_color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
