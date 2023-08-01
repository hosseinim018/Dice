from telethon.sync import TelegramClient, events, Button
from telethon.tl.types import InputMediaDice
from config import api
from Lobby import Lobby
from Player import Player

players = []
lobby = Lobby()



proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', api['api_id'], api['api_hash'], proxy=proxy).start(bot_token=api['bot_token'])


@Client.on(events.NewMessage(pattern='/join'))
async def join(event):
    # players.append(Player(event.chat_id, ['minimumEven', 'minimumOdd', ]))
    player = Player(event.chat_id)
    lobby.addPlayer(player)
    wallet = player.wallet()
    await event.respond(f'now the total amount of money player {player.id} is ${wallet}.')

@Client.on(events.NewMessage(pattern='/roll'))
async def roll_dice(event):

    dice1 = await Client.send_file(event.chat_id, InputMediaDice('🎲'))
    dice2 = await Client.send_file(event.chat_id, InputMediaDice('🎲'))

    rolls = (dice1.media.value, dice2.media.value)
    lobby.set_rolls(rolls)

    keyboard = [
        [
            Button.text('/start'),
        ],
        [
            Button.text('/roll'),
            Button.text('b button')
        ]
    ]
    # await Client.send_message('my_channel_username', 'Click the button below:', buttons=keyboard)
    keyboard2 = [
        [Button.inline('Second button' , b'roll')],
    ]
    # await Client.send_message(event.chat_id, 'Choose an option:', buttons=keyboard)
    await event.respond(f"The dice1 rolled: {dice1.media.value}", buttons=keyboard)
    await event.respond(f"The dice2 rolled: {dice2.media.value}", buttons=keyboard2)
    await event.respond(f"the amount of lobby is: {lobby.amount()}")

    players = lobby.players
    lobby.pay()
    for player in players:
        if event.chat_id == player.id:
            wallet = player.wallet()
            await event.respond(f'now the total amount of money player {player.id} is ${wallet}.')


@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    print(f"The dice rolled: {value}")



with Client:
    Client.run_until_disconnected()
