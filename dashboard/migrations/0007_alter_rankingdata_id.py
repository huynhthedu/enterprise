# Generated by Django 4.2.16 on 2024-12-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_rankingdata_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rankingdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]