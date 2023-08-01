from Payout import payout
class Lobby:
    players: list = []
    def __int__(self, rolls: tuple):
        self.rolls: tuple = rolls

    def addPlayer(self, player):
        self.players.append(player)
        print(f'player {player.id} joined to the laby')

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
            total_factor += factor
        return total_factor

    def pay(self):
        factor = self.get_factors()
        lobby_amount = self.amount()
        amount = lobby_amount/factor
        for player in self.players:
            factor = player.factor()
            pay = amount * factor
            player.pay(pay)

