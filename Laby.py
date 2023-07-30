class laby:
    players: list = []
    def __int__(self):
        pass
    def addPlayer(self, player):
        self.players.append(player)

    def amount(self):
        """
            amount return total amount in laby
            :return a number that is amount
        :return:
        """
        amount = 0
        for player in self.players:
            amount += player.bet

        return amount