from telethon.sync import TelegramClient, events, Button

api = {
    'api_id':'',
    'api_hash':'',
    'bot_token':'968534296:AAG6OR6RNnBKhwLk8DR1b6SjIoSVUpTxu6Y'
}
proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', int(api['api_id']), api['api_hash']).start(bot_token=api['bot_token'])

@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    print(f"The dice rolled: {value}")


with Client:
    Client.run_until_disconnected()
