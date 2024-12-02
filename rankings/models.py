from django.db import models

class EconomicData(models.Model):
    state = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    indicator = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    year = models.IntegerField()
    value = models.FloatField()

    class Meta:
        unique_together = ('state', 'indicator', 'year')
        ordering = ['state', 'year']

    def __str__(self):
        return f"{self.state} - {self.indicator} ({self.year})"


class Indicator(models.Model):
    state = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    indicator = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    year = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return f"{self.state} - {self.indicator} ({self.year})"
    

class IndicatorIndex(models.Model):
    group = models.CharField(max_length=20)
    indicator = models.CharField(max_length=200)
    weight = models.FloatField(default=1/25)

    def __str__(self):
        return f"{self.group} - {self.indicator}"
    
class GroupName(models.Model):
    index = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    weight = models.FloatField(default=1/6)

    def __str__(self):
        return f"{self.index} - {self.name}"
