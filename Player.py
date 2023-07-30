class Player:
    def __init__(self, id, betList):
        self.amount= {
            'wallet': 50_000,
            'bet': 0
        }
        self.id = id
        self.betList = betList

    def wallet(self):
        return self.amount['wallet']

    def bet(self, num: int):
        self.amount['bet'] = num
        self.amount['wallet'] -= num
        return self.amount['bet']

