#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "3599592"
API_HASH = "80865dfca1e192f81931cbf61203cfe7"
BOT_TOKEN = "5619111521:AAFrXFWYqnFT16cloXdga-x2YUn8-x8rUQI"
SESSION = "BQBqOLTAFJKA12k6Qx5sWenbV2Q4cIF44310BV7Lqvod6nKqG-CWuKK7"
FORCESUB = "DroneBots"
AUTH = 1058482162

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
