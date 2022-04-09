from .config import Config
from slack_bolt import App

app = App(token=Config.SLACK_BOT_TOKEN, 
          signing_secret=Config.SLACK_SIGNING_SECRET) 

if __name__ == '__main__':
    app.start(port=Config.PORT)