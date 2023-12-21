from telethon import TelegramClient
from telethon.tl.types import PeerChannel
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env')

# Use your own values from my.telegram.org
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')


bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
client = TelegramClient('anon', api_id, api_hash)

bicone = PeerChannel(channel_id=-1391071493)

with bot:
    bot.loop.run_until_complete(bot.send_message(bicone, 'I am agonizing from the pains of childbirth!'))
