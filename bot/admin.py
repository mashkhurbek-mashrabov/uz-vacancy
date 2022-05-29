from django.contrib import admin

from bot.models.bot import TelegramBotUser
from bot.models.vacancy import Category, Detail, Vacancy, DetailValue, DetailSelection


@admin.register(TelegramBotUser)
class TelegramBotUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'chat_id', 'step']
    search_fields = ['name', 'chat_id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'status']
    list_filter = ['category', 'status']
    search_fields = ['user']


@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'ordering', 'detail_type', 'is_active']
    list_filter = ['category', 'detail_type']
    search_fields = ['title']


@admin.register(DetailValue)
class DetailValueAdmin(admin.ModelAdmin):
    list_display = ['value', 'vacancy', 'category']
    list_filter = ['category', 'vacancy__status']
    search_fields = ['value']


@admin.register(DetailSelection)
class DetailSelectionAdmin(admin.ModelAdmin):
    list_display = ['value', 'is_active']
    list_filter = ['detail__category', 'detail__detail_type', 'is_active']
    search_fields = ['value']
