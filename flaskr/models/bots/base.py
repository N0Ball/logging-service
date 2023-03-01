from flaskr.main import app

class Bot:

    def __init__(self, prefix:str):
        self.PREFIX = prefix.upper()
        self.CONFIG = {}

        for config in self.REQUIRED_CONFIGS:
            
            self.CONFIG.update({
                config: app.config.get(
                f'{self.PREFIX}_{config}'
                )
            })

    def send_message(self,msg:str) -> int:
        pass