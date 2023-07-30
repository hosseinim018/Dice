from telethon.sync import TelegramClient, events, Button
from telethon.tl.types import InputMediaDice
from config import api

proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', api['api_id'], api['api_hash'], proxy=proxy).start(bot_token=api['bot_token'])

@Client.on(events.NewMessage(pattern='/roll'))
async def roll_dice(event):
    dice = await Client.send_file(event.chat_id, InputMediaDice('🎲'))
    print(dice)
    print('---------')
    value = dice.media.value
    print(f"The dice rolled: {value}")

@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    print(f"The dice rolled: {value}")


with Client:
    Client.run_until_disconnected()
