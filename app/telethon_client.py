from telethon import TelegramClient, events
from datetime import datetime
from cfg import *

api_id = API_ID
api_hash = API_HASH
client = TelegramClient('bot', api_id, api_hash)
