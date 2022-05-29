from django.db import models

from bot.constants.vacancy import VacancyStatusChoices, DetailTypes
from bot.models.bot import TelegramBotUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    status = models.IntegerField(choices=VacancyStatusChoices.choices)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vacancies')
    user = models.ForeignKey(TelegramBotUser, on_delete=models.CASCADE, related_name='vacancies')


class Detail(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=256)
    emoji = models.CharField(max_length=64)
    ordering = models.IntegerField()
    detail_type = models.IntegerField(choices=DetailTypes.choices)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='details')

    def __str__(self):
        return self.title


class DetailValue(models.Model):
    value = models.CharField(max_length=500)

    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='detail_values')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='detail_values')


class DetailSelection(models.Model):
    value = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, related_name='selections')
