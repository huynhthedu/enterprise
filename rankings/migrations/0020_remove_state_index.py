# Generated by Django 4.2.16 on 2024-12-28 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0019_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='index',
        ),
    ]