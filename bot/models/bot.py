from django.db import models


class TelegramBotUser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    chat_id = models.CharField(max_length=100, unique=True)
    step = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.chat_id} - {self.name}"
