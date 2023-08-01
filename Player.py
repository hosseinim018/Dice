class Player:
    def __init__(self, id):
        self.amount = {
            'wallet': 50_000,
            'bet': 0
        }
        self.id = id
        self.betList = []
        self.factor = 0

    def wallet(self):
        return self.amount['wallet']

    def bet(self, num: int):
        self.amount['bet'] = num
        self.amount['wallet'] -= num
        return self.amount['bet']

    def getBetAmount(self):
        return self.amount['bet']

    def pay(self, pay:int):
        """
        this method increase amount wallet
        :param pay: amount add with wallet amount
        """
        self.amount['wallet'] += pay

    def get_factor(self):
        return self.factor

    def set_betlist(self, bet:str):
        self.betList.append(bet)



