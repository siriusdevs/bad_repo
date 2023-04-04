from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.db.models import TextChoices
from datetime import date, datetime


class AgeValidator(BaseValidator):
    def __call__(self, age: int):
        if age < 0:
            raise ValidationError(
                f'Age {age} is less than zero',
                params={'age': age}
            )

class PersonStatus(TextChoices):
    STUDENT = 'student', 'student'
    EMPLOYED = 'employed', 'employed'
    UNEMPLOYED = 'unemployed', 'unemployed'

CF_DEFAULT= 30

class PersonManager(models.Manager):
    def create_from_birthdate(self, name: str, birthdate: date):
        now = datetime.now()
        age = now.year - birthdate.year
        if now.month < birthdate.month or (now.month == birthdate.month and now.day < birthdate.day):
            age -= 1
        return self.create(name=name, age=age)

class Person(models.Model):
    id = models.UUIDField(editable=False, default=uuid4, primary_key=True, blank=False, null=False)
    name = models.CharField(max_length=CF_DEFAULT, blank=False, null=False, db_index=True)
    age = models.IntegerField(validators=(AgeValidator,), blank=False, null=False)
    status = models.CharField(
        choices=PersonStatus.choices, 
        default = PersonStatus.UNEMPLOYED,
        max_length=CF_DEFAULT, 
        blank=False, 
        null=False
    )
    objects = PersonManager()

    def __str__(self):
        return f'{self.id}, {self.name}, {self.age}'


