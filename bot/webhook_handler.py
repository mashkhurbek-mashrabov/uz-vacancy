import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot.constants.bot import BOT_TOKEN
from bot.controllers.main import BotController

bot = telebot.TeleBot(BOT_TOKEN)


@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        bot.process_new_updates(
            [telebot.types.Update.de_json(
                request.body.decode("utf-8"))
            ]
        )
        return HttpResponse(status=200)
    else:
        return HttpResponse('.')


@bot.message_handler(commands=['start'])
def start_handler(message):
    controller = BotController(message, bot)
    controller.greeting()


@bot.message_handler(content_types=['text'])
def message_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step
    message_text = message.text


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(callback):
    controller = BotController(callback, bot)
    user_step = controller.step
    callback_data = callback.data


@bot.message_handler(content_types='contact')
def contact_handler(phone):
    controller = BotController(phone, bot)
    user_step = controller.step


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'sticker'])
def content_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step
