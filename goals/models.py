from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GoalStatus(models.Model):
    status_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.status_name 

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length = 30)
    goal_id = models.IntegerField( default = 1)
    created_by = models.CharField(max_length = 30)
    moved_by = models.CharField(max_length = 30)
    owner = models.CharField(max_length = 30)
    goal_status = models.ForeignKey(
        GoalStatus,
        on_delete = models.PROTECT
    ) 
    user = models.ForeignKey(
        User,
        related_name = 'ScrumyGoals',
        on_delete = models.PROTECT
    )

    def __str__(self):
        return self.goal_name
       
