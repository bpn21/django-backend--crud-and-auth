# Generated by Django 3.1.2 on 2020-11-05 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20201105_0513'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Person',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='person',
        ),
    ]
