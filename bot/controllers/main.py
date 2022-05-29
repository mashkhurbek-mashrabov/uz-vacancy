from bot.controllers.base import BaseController


class BotController(BaseController):
    def greeting(self):
        self.sync_user()
        self.send_message(message_text=self.messages('greeting'))