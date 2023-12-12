from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=50)
    max_visitors = models.IntegerField()
    current_visitors = models.IntegerField(default=0)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='location')
    
    def __str__(self):
        return f"{self.name} - {self.ad.name}"
    