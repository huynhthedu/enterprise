# dashboard/models.py

from django.db import models

# dashboard/models.py

class RankingData(models.Model):
    Indicator = models.CharField(max_length=255, default='N/A')
    Rank_2010 = models.IntegerField()
    Rank_Growth_2010_2019 = models.IntegerField()
    Rank_2019 = models.IntegerField()
    Rank_Growth_2019_2023 = models.IntegerField()
    Rank_2023 = models.IntegerField()
    State = models.CharField(max_length=255, default='N/A', null=True, blank=True)  # Make optional

    def __str__(self):
        return self.Indicator