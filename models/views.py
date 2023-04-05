from django.shortcuts import render
from .models import Person
from django.db import transaction
from django.views import View

BASE_TEMPLATE = 'base.html'

@transaction.atomic(using='default')
def default(request):
    print(Person.objects.all())
    print(request.GET)
    objects = Person.objects.filter(name='Vasya')
    print(objects)
    return render(
        request,
        BASE_TEMPLATE,
        context={
            'objects': objects
        }
    )

@transaction.atomic(using='backup')
def backup(request):
    return render(
        request,
        BASE_TEMPLATE,
        context={
            'objects': Person.objects.filter(**request.GET)
        }
    )