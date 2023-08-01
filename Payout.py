class payout:
    def __init__(self, rolls: tuple, predict: list):
        """
         Args:
                rolls(tuple): rolls have 2 index rolls number 1 and 2
                predict(list): user predicts for bet
        """
        self.rolls = rolls
        self.predict = predict
    def isEven(self, num:int) -> bool:
        """
            this function check a number is even or odd

            Args:
                num (int): the number of dice rolled

            Returns:
                boolean (bool): if number be even return True else False
        """
        if num % 2 == 0:
            return True
        else:
            return False

    def checkGusses(self) -> dict:
        """
            Determine whether the user has gussed the correct
            Returs:
                guesses (dict): ---
        """
        num_roll1, num_roll2 = self.rolls
        # check roll1/2 is even/odd 
        roll1, roll2 = self.isEven(num_roll1), self.isEven(num_roll2)
        guesses = {
            'minimumEven': False,
            'minimumOdd': False,
            'maximumEven': False,
            'maximumOdd': False,
            'roll1Even': roll1,
            'roll2Even': roll2,
            'sumEven': self.isEven(num_roll1 + num_roll2)
        }
        # check condition of possible minimum even/odd
        if roll1 == True or roll2 == True:
            guesses['minimumEven'] = True
        if roll1 == False or roll2 == False:
            guesses['minimumOdd'] = True
        # check condition of possible maximum even/odd
        if roll1 == True and roll2 == True:
            guesses['maximumEven'] = True
        if roll1 == False and roll2 == False:
            guesses['maximumOdd'] = True

        return guesses
    def factor(self):
        guesses = self.checkGusses()
        # check validaton predicts
        win = True
        factor = 1
        risks = {
            'minimumEven': 1 / 2,
            'minimumOdd': 1 / 2,
            'maximumEven': 1 / 2,
            'maximumOdd': 1 / 2,
            'roll1Even': 1 / 2,
            'roll2Even': 1 / 2,
            'sumEven': 1 / 2,
        }
        for i in self.predict:
            if guesses[i]:
                print(risks[i] + 1)
                factor *= (risks[i] + 1)
            else:
                print('you lose because once of your bets incorrect')
                print(f'incorrect bet: {i}')
                win = False
                break
        if win:
            print('you win', factor)
            return factor




