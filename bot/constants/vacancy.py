from django.db import models


class VacancyStatusChoices(models.IntegerChoices):
    NEW = 1
    WAITING_FOR_CONFIRMATION = 2
    ACTIVE = 3
    PASSIVE = 4
    DECLINED = 5


class DetailTypes(models.IntegerChoices):
    STRING = 1
    INTEGER = 2
    PHOTO = 3
    SELECT = 4
