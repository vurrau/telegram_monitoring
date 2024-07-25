from telethon import events

from telethon_client import client
from models import SessionLocal, Message

bot = client


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Hello! Use /latest to get the latest messages.')


@bot.on(events.NewMessage(pattern='/latest'))
async def latest(event):
    db = SessionLocal()
    messages = db.query(Message).order_by(Message.date.desc()).limit(10).all()
    db.close()
    response = "\n".join(
        [f"{msg.date} - {msg.first_name or ''} {msg.last_name or ''}: {msg.text}" for msg in messages]
    )
    await event.respond(response)


def start_bot():
    bot.run_until_disconnected()

