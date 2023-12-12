from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ManyToManyField('Location', related_name='ads')
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=50)
    max_visitors = models.IntegerField()
    current_visitors = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.ad.name}"
    
class VisitCount(models.Model):
    date = models.DateField()
    count = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='visit_counts')
    