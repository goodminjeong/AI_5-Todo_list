# Generated by Django 4.2 on 2023-04-28 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_rename_user_todo_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user_id',
            new_name='user',
        ),
    ]