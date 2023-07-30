from telethon.sync import TelegramClient, events, Button
from telethon.tl.types import InputMediaDice
import api from config

proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', api['api_id'], api['api_hash'], proxy=proxy).start(bot_token=api['bot_token'])

@Client.on(events.NewMessage(pattern='/roll'))
async def roll_dice(event):
    dice = InputMediaDice('🎲')
    await Client.send_file(event.chat_id, dice)
@Client.on(events.NewMessage(func=lambda m: m.media))
async def handle(event):
    print(event)

@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    print(f"The dice rolled: {value}")
    print(event.message)
    print(event.message.dice)


with Client:
    Client.run_until_disconnected()
