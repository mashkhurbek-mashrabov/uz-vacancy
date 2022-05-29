# Generated by Django 4.0.4 on 2022-05-29 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=256)),
                ('emoji', models.CharField(max_length=64)),
                ('ordering', models.IntegerField()),
                ('detail_type', models.IntegerField(choices=[(1, 'String'), (2, 'Integer'), (3, 'Photo'), (4, 'Select')])),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='bot.category')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramBotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(max_length=100, null=True)),
                ('chat_id', models.CharField(max_length=100, unique=True)),
                ('step', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'New'), (2, 'Waiting For Confirmation'), (3, 'Active'), (4, 'Passive'), (5, 'Declined')])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='bot.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='bot.telegrambotuser')),
            ],
        ),
        migrations.CreateModel(
            name='DetailValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_values', to='bot.category')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_values', to='bot.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='DetailSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=128)),
                ('is_active', models.BooleanField(default=True)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='bot.detail')),
            ],
        ),
    ]