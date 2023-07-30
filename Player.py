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

    def getBetAmount(self):
        return self.amount['bet']

    def validation(self, roll1, roll2):
        totalFactor = 1
        for bet in self.betList:
            query = bet['query']
            message = bet['message']
            factor = bet['factor']
            message = f'the player {self.id} wid: {query}, {message}'
            if query == 1:
                if roll1 % 2 == 0 and roll2 % 2 == 0:
                    totalFactor *= factor

            if query == 2:
                if roll1 % 2 != 0 and roll2 % 2 != 0:
                    totalFactor *= factor
            if query == 3:
                if roll1 % 2 == 0 or roll2 % 2 == 0:
                    totalFactor *= factor

            if query == 4:
                if roll1 % 2 != 0 or roll2 % 2 != 0:
                    totalFactor *= factor

            if query == 5:
                if roll1 % 2 == 0:
                    totalFactor *= factor

            if query == 6:
                if roll2 % 2 == 0:
                    totalFactor *= factor

            if query == 7:
                if roll1 % 2 != 0:
                    totalFactor *= factor

            if query == 8:
                if roll2 % 2 != 0:
                    totalFactor *= factor

            if query == 9:
                if (roll1 + roll2) % 2 == 0:
                    totalFactor *= factor

            if query == 10:
                if (roll1 + roll2) % 2 != 0:
                    totalFactor *= factor

        self.amount['wallet'] = self.amount['wallet'] * totalFactor

