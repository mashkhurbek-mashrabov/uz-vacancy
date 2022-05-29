import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

messages = {
    'greeting': "Assalomu alaykum!",
    'main menu': '⏏️ Asosiy menu',
    'back_button': '⬅️ Ortga',
    'cancel': "❌ Bekor qilish",
}


class BotUserSteps:
    GET_CATEGORY = 1


class CallbackData:
    main_menu_button = 'main menu'
    back_button = 'back button'
    cancel_button = 'cancel button'
    confirm = 'confirm'
    decline = 'decline'
    sold_out = 'sold_out'
