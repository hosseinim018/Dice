class payout:
    def __init__(self):
        pass

    def checkEven(self, num:int)->bool:
        """
            this function check a number is even or odd
            :return boolean if number be even return True else False
        """
        if num % 2 == 0:
            return True
        else:
            return False