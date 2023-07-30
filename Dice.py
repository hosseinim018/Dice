from telethon.sync import TelegramClient, events, Button
import socks
api = {
    'api_id':1719463,
    'api_hash':'a4517a41ddb3b3c8bd544e45db0a7dc3',
    'bot_token':'968534296:AAG6OR6RNnBKhwLk8DR1b6SjIoSVUpTxu6Y'
}

proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', api['api_id'], api['api_hash'], proxy=proxy).start(bot_token=api['bot_token'])

@Client.on(events.NewMessage(pattern='/roll'))
async def roll_dice(event):
    await Client.send_message(event.chat_id, '/dice')


@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    print(f"The dice rolled: {value}")


with Client:
    Client.run_until_disconnected()
