from Payout import payout
class Lobby:
    def __init__(self):
        self.players: list = []

    def set_rolls(self, rolls: tuple):
        self.rolls: tuple = rolls

    def addPlayer(self, player):
        self.players.append(player)
        # print(f'player {player.id} joined to the lobby')

    def get_playerID(self):
        players_id = [player.id for player in self.players]
        return players_id

    def amount(self):
        """
            amount return total amount in laby
            :return a number that is amount
        :return:
        """
        amount = 0
        for player in self.players:
            betAmount = player.getBetAmount()
            amount += betAmount

        return amount

    def get_factors(self):
        total_factor = 0
        for player in self.players:
            pay = payout(self.rolls, player.betList)
            factor = pay.factor()
            player.factor = factor
            if factor != None:
                total_factor += factor
        if total_factor == 0:
            return 1
        else:
            return total_factor

    def pay(self):
        factor = self.get_factors()
        lobby_amount = self.amount()
        amount = lobby_amount / factor
        total_pay = 0
        for player in self.players:
            factor = player.factor
            if factor != None:
                # print('factor', factor)
                pay = amount * factor
                total_pay += pay
                player.pay(pay)

        self.players: list = []
