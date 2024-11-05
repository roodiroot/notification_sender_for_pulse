import os
from dotenv import load_dotenv

from models.models import Case
from datetime import datetime, timedelta

load_dotenv()

def get_all_tasks():
    tasks = (Case
         .select()) 
    return tasks

def get_tasks_by_time(current_time: datetime) -> list[Case]:
    adjusted_time = current_time - timedelta(hours=int(os.getenv("UTG")))
    tasks = Case.select().where(Case.date == adjusted_time)
    return tasks
