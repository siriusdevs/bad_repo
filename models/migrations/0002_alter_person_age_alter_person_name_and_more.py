# Generated by Django 4.1.7 on 2023-04-04 08:35

from django.db import migrations, models
import models.models as my_models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(validators=[my_models.AgeValidator]),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('student', 'student'), ('employed', 'employed'), ('unemployed', 'unemployed')], default='unemployed', max_length=30),
        ),
    ]
