from django.db import migrations

def convert_non_numeric_to_numeric(apps, schema_editor):
    Indicator = apps.get_model('rankings', 'Indicator')
    for obj in Indicator.objects.all():
        try:
            obj.value = float(obj.value)
            obj.save()
        except ValueError:
            obj.value = 0  # Example: set non-numeric values to 0
            obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('rankings', '0002_indicator'),  # Update with the correct initial migration name
    ]

    operations = [
        migrations.RunPython(convert_non_numeric_to_numeric),
    ]