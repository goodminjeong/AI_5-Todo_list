# Generated by Django 4.2 on 2023-04-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='완료일'),
        ),
    ]
