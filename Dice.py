from telethon.sync import TelegramClient, events, Button
from telethon.tl.types import InputMediaDice
from config import api
from Lobby import Lobby
from Player import Player
import re
from random import randint

def generate_dice():
    dices = {
        i: f'animateddice/tgs/{i}.tgs' for i in range(1, 7)
    }
    dice_number = randint(1, 6)
    file_path = dices[dice_number]
    return dice_number, file_path

lobby = Lobby()

proxy = ("socks5", '127.0.0.1', 10808)

Client = TelegramClient('Dice_session', api['api_id'], api['api_hash'], proxy=proxy).start(bot_token=api['bot_token'])

@Client.on(events.NewMessage(pattern='/start'))
async def start(event):
    msg = "wellcome to the bot"
    keyboard = [
        [
            Button.text('/start'),
            Button.text('/test'),
        ],
        [
            Button.text('/join'),
            Button.text('/roll'),
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
    betlist = ['minimumEven','minimumOdd','maximumEven','maximumOdd','roll1Even','roll2Even','sumEven']
    # bet.encode('utf-8')
    keyboard = [[Button.inline(bet , f"betlist-{bet}".encode('utf-8'))] for bet in betlist]
    await event.respond(f'the number of players is: {len(lobby.players)}')
    await event.respond(f'the total amount of money player {player.id} is ${wallet} with bet with amount {bet}\nchoose your bets', buttons=keyboard)

@Client.on(events.NewMessage(pattern='/roll'))
async def roll_dice(event):
    lobby_amount = lobby.amount()
    dice_number1, file_path1 = generate_dice()
    dice_number2, file_path2 = generate_dice()
    if len(lobby.players) >= 2:
        for player in lobby.players:

            rolls = (dice_number1, dice_number2)
            lobby.set_rolls(rolls)

            await Client.send_message(player.id, file=file_path1)
            await Client.send_message(player.id, file=file_path2)
            await Client.send_message(player.id, f"The dice1 rolled: {dice_number1}\nThe dice2 rolled: {dice_number2}")
            await Client.send_message(player.id, f"the amount of lobby is: {lobby_amount}")
            # print(player.betList)
            if len(player.betList) == 0:
                await event.respond('you should set a bet List. press /join')
            else:
                lobby.pay()
                wallet = player.wallet()
                await Client.send_message(player.id, f'now the total amount of money player {player.id} is ${wallet}.')
    else:
        await event.respond('the number of players for play is not enough, wait or invait your friends')


# @Client.on(events.NewMessage(pattern='/test'))
@Client.on(events.NewMessage(func=lambda event: event.dice))
async def handle_dice(event):
    value = event.message.dice.value
    event.respond(f"The dice rolled: {value}")



@Client.on(events.CallbackQuery())
async def handle_callback_query(event):
    data = event.data.decode()
    # Use the `search` function to find the bet prefix in the string
    betlist = re.search('betlist', data)
    # Define the regex pattern to match the characters after the 'betlist-' prefix
    pattern = r'betlist-(.*)'
    # Use the `search` function to find the characters after the 'betlist-' prefix in the string
    bet = re.search(pattern, data)

    # Check if the match was found
    if betlist and bet:
        bet_prefix = betlist.group()
        bet_id = bet.group(1)
        for player in lobby.players:
            if player.id == event.chat_id:
                msg = f"you secelet this {bet_id} bet"
                await event.respond(msg)
                player.set_betlist(bet_id)

with Client:
    Client.run_until_disconnected()
