from telethon import TelegramClient, events
from datetime import datetime

from models import Message, SessionLocal
from cfg import *

api_id = API_ID
api_hash = API_HASH
client = TelegramClient('bot', api_id, api_hash)


@client.on(events.NewMessage)
async def handler(event):
    print(f"Received a new message from {event.sender_id}: {event.text}")
    sender = await event.get_sender()
    message = Message(
        message_id=event.id,
        text=event.text,
        sender_id=sender.id,
        first_name=sender.first_name,
        last_name=sender.last_name,
        username=sender.username,
        phone_number=sender.phone,
        date=datetime.now()
    )
    db = SessionLocal()
    db.add(message)
    db.commit()
    db.close()


def start_client():
    client.start()
    client.run_until_disconnected()