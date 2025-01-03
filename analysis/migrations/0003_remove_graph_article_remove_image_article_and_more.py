# Generated by Django 4.2.16 on 2024-12-24 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_worddocument'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graph',
            name='article',
        ),
        migrations.RemoveField(
            model_name='image',
            name='article',
        ),
        migrations.DeleteModel(
            name='WordDocument',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(default=1, upload_to='pdfs/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Graph',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
