# Generated by Django 4.2.16 on 2024-12-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_article_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(upload_to='images/'),
        ),
    ]