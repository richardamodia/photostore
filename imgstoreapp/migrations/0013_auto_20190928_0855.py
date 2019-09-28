# Generated by Django 2.2.5 on 2019-09-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgstoreapp', '0012_imageclone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageclone',
            old_name='img_height',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='imageclone',
            old_name='img_width',
            new_name='width',
        ),
        migrations.AddField(
            model_name='imageclone',
            name='crop_to_fit',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
