"""Use this file with: python3 manage.py shell < main.py"""
from models.models import Person
from django.db.models import Max, Count, Q, Min, Avg
from datetime import date


# custom method defined in our objects manager
first_person = Person.objects.create_from_birthdate(name='Ivan', birthdate=date(1983, 2, 15))
print(f'Person created and saved to DB: {first_person}')

# get is a default manager method, we are getting a person we just created
first_person_db = Person.objects.get(id=first_person.id)
print(f'Person record stored in DB: {first_person_db}')

# deleting this person from database
first_person_db.delete()

# check if the person is stil in DB
vanya_present = Person.objects.contains(first_person)
print(f'Does DB have this person after deleting? - {vanya_present}')

# aggregate by default returns dict of values, specified in its args
# this example shows statistics of max, min and average age among persons in DB
aggr = Person.objects.aggregate(max_age=Max('age'), min_age=Min('age'), avg_age=Avg('age'))
print(aggr)

# aggregate by default returns dict of values, specified in its args
# this example shows age difference between the oldest and the youngest person in DB
age_diff = Person.objects.aggregate(age_diff=Max('age') - Min('age'))
print(age_diff)

# filter method can use complex filter statements
ivans = Person.objects.filter(name__startswith='Ivan')
print(ivans)

# annotate method by default returns QuerySet of model objects
# this example returns all adults among persons in DB
# Q is just an object incapsulation
adults = Person.objects.annotate(adults=Count('age', filter=Q(age__gt=18)))
print(type(adults))
for adult in adults:
    print(adult)