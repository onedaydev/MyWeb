# Generated by Django 4.1.3 on 2022-12-24 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_title_todo_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='label',
            new_name='title',
        ),
    ]