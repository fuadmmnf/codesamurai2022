from django.db import models


# Create your models here.
class UserType(models.Model):
    code = models.CharField(max_length=32)
    committee = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)


class User(models.Model):
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=512)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)


class Agency(models.Model):
    code = models.CharField( max_length=32)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=32)
    description = models.CharField(max_length=1000)


class Project(models.Model):
    project_id = models.CharField(max_length=32)
    exec = models.ForeignKey(Agency, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    start_date = models.DateField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    cost = models.FloatField()
    timespan = models.FloatField()
    feedback = models.CharField(max_length=1000, default='')
    rating = models.IntegerField(null=True)
    goal = models.CharField(max_length=1000)
    completion = models.FloatField(null=True)
    actual_cost = models.FloatField(null=True)
    is_accepted = models.BooleanField(default=True)
    proposal_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)


class Component(models.Model):
    component_id = models.CharField(max_length=32)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    executing_agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    component_type = models.CharField(max_length=32)
    depends_on = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    budget_ratio = models.FloatField()


class Constraint(models.Model):
    constraint_type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)
    max_limit = models.IntegerField()
