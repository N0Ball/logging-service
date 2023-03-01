import json
import requests

from .base import Bot

class TelegramBot(Bot):

    def __init__(self):
        self.REQUIRED_CONFIGS = ['SECRET', 'CHATID']
        super().__init__(__name__.split('.')[-1])

    def send_message(self,msg:str) -> int:

        headers = {
            'Content-Type': 'application/json'
        }
        data_dict = {
            'chat_id': self.CONFIG.get('CHATID'),
            'text': msg,
            'parse_mode': 'HTML'
        }

        data = json.dumps(data_dict)
        url = f'https://api.telegram.org/bot{self.CONFIG.get("SECRET")}/sendMessage'

        response = requests.post(
            url,
            data=data,
            headers=headers,
        )

        if response.status_code == 200:
            return 1

        return -1