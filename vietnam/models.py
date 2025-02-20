from django.db import models

# Create your models here.
class VnData(models.Model):
    id_key = models.IntegerField(db_column='id_key', blank=True, null=False, unique=True, primary_key=True)  
    id = models.CharField(db_column='id', max_length=50, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(db_column='group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='year', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VN_data'


class VnIndicators(models.Model):
    index = models.CharField(db_column='id', max_length=50, blank=True, null=False, unique=True, primary_key=True)  # Field name made lowercase.    
    group = models.CharField(db_column='group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    indicators = models.CharField(db_column='indicators', max_length=128, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='unit', max_length=50, blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='weight', blank=True, null=True)  # Field name made lowercase.    
    status = models.IntegerField(db_column='status', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='source', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VN_indicators'


class VnProvince(models.Model):
    id = models.CharField(db_column='id', max_length=50, blank=True, null=False, unique=True, primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='region', max_length=50, blank=True, null=True)  # Field name made lowercase.
    province = models.CharField(db_column='province', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VN_province'

class VnGroup(models.Model):
    id = models.CharField(db_column='id', max_length=50, blank=True, null=False, unique=True, primary_key=True)  # Field name made lowercase.
    group = models.CharField(db_column='group', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='indicators', max_length=128, blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='weight', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VN_group'