class Lobby:
    players: list = []
    def __int__(self):
        pass
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