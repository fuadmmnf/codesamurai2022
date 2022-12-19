from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    affiliated_agency = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    project_start_time = models.DateField()
    project_completion_time = models.DateField()
    total_budget = models.CharField(max_length=32)
    completion_percentage = models.CharField(max_length=32)
    location_coordinates = models.CharField(max_length=1000)
