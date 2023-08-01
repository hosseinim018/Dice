from telethon.sync import TelegramClient, events, Button
from telethon.tl.types import InputMediaDice
from config import api
from Lobby import Lobby
from Player import Player


lobby = Lobby()

proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', api['api_id'], api['api_hash'], proxy=proxy).start(bot_token=api['bot_token'])

@Client.on(events.NewMessage(pattern='/start'))
async def start(event):
    msg = "wellcome to the bot"
    keyboard = [
        [
            Button.text('/start'),
        ],
        [
            Button.text('/join'),
            Button.text('/roll'),
            Button.text('/betlist'),
            Button.text('/wallet')
        ]
    ]
    await event.respond(msg, buttons=keyboard)

@Client.on(events.NewMessage(pattern='/join'))
async def join(event):
    player = Player(event.chat_id)
    lobby.addPlayer(player)
    wallet = player.wallet()
    bet = player.bet(10_000)
    await event.respond(f'the number of players is: {len(lobby.players)}')
    await event.respond(f'the total amount of money player {player.id} is ${wallet} with bet with amount {bet}')

@Client.on(events.NewMessage(pattern='/roll'))
async def roll_dice(event):
    if len(lobby.players)>2:
        for player in lobby.players:
            if player.id == event.chat_id:
                dice1 = await Client.send_file(event.chat_id, InputMediaDice('🎲'))
                dice2 = await Client.send_file(event.chat_id, InputMediaDice('🎲'))

                rolls = (dice1.media.value, dice2.media.value)
                lobby.set_rolls(rolls)

                await event.respond(f"The dice2 rolled: {dice2.media.value}\nThe dice1 rolled: {dice1.media.value}", buttons=keyboard2)
                await event.respond(f"the amount of lobby is: {lobby.amount()}")
                if len(player.betList) == 0:
                    await event.respond('you should set a bet List. press /betlist')
                else:
                    lobby.pay()
                    wallet = player.wallet()
                    await event.respond(f'now the total amount of money player {player.id} is ${wallet}.')
        else:
            await event.respond('first you should join to a lobby.\npress /join')
    else:
        await event.respond('the number of players for play is not enough, wait or invait your friends')


@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    event.respond(f"The dice rolled: {value}")

@Client.on(events.NewMessage(pattern='/betlist'))
async def Betlist(event):
    msg = """"""
    betlist = ['minimumEven','minimumOdd','maximumEven','maximumOdd','roll1Even','roll2Even','sumEven']
    # bet.encode('utf-8')
    keyboard = [[Button.inline(bet , 'betlist')] for bet in betlist]
    await event.respond(msg, buttons=keyboard)

@Client.on(events.CallbackQuery())
async def handle_callback_query(event):
    # Get the callback data from the event
    data = event.data.decode()
    if data == 'betlist':
        print(event)
        print(event.message.text)
        for player in lobby.players:
            if player.id == event.chat_id:
                player.set_betlist(event.message.text)
        # msg = Client.get_messages(event.chat_id, ids=event.message_id)
        # print(msg)

with Client:
    Client.run_until_disconnected()
