# Generated by Django 4.0.10 on 2023-03-11 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='chef',
            new_name='chef_user',
        ),
    ]
