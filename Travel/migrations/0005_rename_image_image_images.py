# Generated by Django 4.1.6 on 2023-02-10 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='images',
        ),
    ]