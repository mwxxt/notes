from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )
    gender = models.CharField('Пол', max_length=1, choices=GENDERS)
    birth_date = models.DateField('Дата рождения')