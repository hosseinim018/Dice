class payout:
    def __init__(self):
        pass

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

    def checkGusses(self,rolls: tuple):
        """
            Determine whether the user has gussed the correct
            Args:
                rolls(tuple): rolls have 2 index rolls number 1 and 2
            Returs:
                gusses (dict): ---
        """
        num_roll1, num_roll2 = rolls
        # check roll1/2 is even/odd 
        roll1, roll2 = self.isEven(num_roll1), self.isEven(num_roll2)
        gusses = {
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
            gusses['minimumEven'] = True
        if roll1 != False or roll2 != False:
            gusses['minimumOdd'] = True
        # check condition of possible maximum even/odd
        if roll1 == True and roll2 == True:
            gusses['maximumEven'] = True
        if roll1 != False and roll2 != False:
            gusses['maximumOdd'] = True


