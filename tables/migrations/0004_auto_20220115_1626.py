# Generated by Django 3.2 on 2022-01-15 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20220115_1548'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='last_name',
        ),
    ]
