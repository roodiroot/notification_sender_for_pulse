from peewee import JOIN
from datetime import datetime, timedelta
from models.models import Case, Deal

def get_all_tasks():
    tasks = (Case
         .select()) 
    return tasks

def get_tasks_by_time(current_time: datetime):
    adjusted_time = current_time - timedelta(hours=3)
    tasks = Case.select().where(Case.date == adjusted_time)
    return tasks