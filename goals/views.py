from django.shortcuts import render
from django.http import HttpResponse 
from  .models import *
import datetime
from random import randint
from django.contrib.auth.models import User


# Create your views here.
def get_grading_parameters(request) :
    # goals2 = ScrumyGoals.objects.filter(goal_name = 'keep learning django')
    goals = 'keep learning django'
    return HttpResponse(goals) 

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)    

def add_goal(request):
      goalId = randint(1000, 9999)
      goalStatus = GoalStatus.objects.last()
      addGoalUser = User.objects.get(username = 'louis')
      addGoal = ScrumyGoals.objects.create(goal_name = 'keep learning django', goal_id = goalId, created_by = 'Louis' , moved_by = 'Louis', owner = 'Louis' , goal_status = goalStatus ,user = addGoalUser ) 
      return HttpResponse(addGoal)