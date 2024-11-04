import uuid
from enum import Enum
from datetime import datetime

from peewee import Model, CharField, DateTimeField, TextField, BooleanField, ForeignKeyField

from db.db_init import db 

# Определение Enum-класса
class ActionType(Enum):
    CALL = "Call"
    BRIEF = "Brief"
    MEET = "Meet"
    EMAIL = "Email"
    TASK = "Task"

# Базовая модель
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=lambda: str(uuid.uuid4()))
    name = CharField(max_length=255, null=True)
    email = CharField(max_length=255, unique=True, null=True)

    class Meta:
        table_name = 'User'

# Определение модели Settings
class Settings(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=lambda: str(uuid.uuid4()))
    telegramChatId = CharField(max_length=255, null=True)
    userId = ForeignKeyField(
        User, field='id', 
        column_name='userId', 
        unique=True, 
        null=True, 
        backref='settings'
        )

class Company(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=lambda: str(uuid.uuid4()))
    name = CharField(max_length=255)
    TIN = CharField(null=True)
    userId = ForeignKeyField(
        User, 
        field='id',
        column_name='userId',
        backref='companies',
        null=True,
        on_delete='CASCADE'
        ) 


class Deal(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=lambda: str(uuid.uuid4()))
    name = CharField(max_length=255)
    contractPrice = CharField(null=True)  # Или IntegerField, если это целое число
    companyId = ForeignKeyField(
        Company,
        field='id',
        column_name='companyId',
        backref='deals',
        null=True,
        on_delete='CASCADE'
    ) # Связь с моделью Deal

# Определение модели Case
class Case(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=lambda: str(uuid.uuid4()))
    createdAt = DateTimeField(default=datetime.now)  # Аналог auto_now_add=True
    type = CharField(max_length=50, default=ActionType.CALL.value)  # Пример Enum, можно создать отдельный Enum-класс
    comment = TextField(null=True)
    date = DateTimeField(null=True)
    responsible = CharField(max_length=255, null=True)
    finished = BooleanField(default=False)
    dealId = ForeignKeyField(
        Deal,
        field='id',
        column_name='dealId',
        backref='cases',
        null=True,
        on_delete='CASCADE'
    ) # Связь с моделью Deal

