from django.db import models

# Create your models here.
class LibraryDimension(models.Model):
    lb_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'library_dimension'
        
