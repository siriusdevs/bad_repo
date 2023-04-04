#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from models.models import Person


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lecture_models.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    vanya = Person.objects.filter(id='8910124f-698c-4da5-983d-bd92a725e97d')
    vanya.delete()
    vanya_present = Person.objects.contains(id='8910124f-698c-4da5-983d-bd92a725e97d')
    print(vanya_present)
    raise SystemExit