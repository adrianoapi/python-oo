class BankBradescoAccount(object):
    
    def __init__(self, number):
        self.number = number
        self.__total = 0
        
    def deposit(self, value):
        self.__total += value
        
    def withdraw(self, value):
        self.__total -= value
        self.__total -= 1
        
    def get_total(self):
        return self.__total

class BankItauAccount(BankBradescoAccount):
    #pass
    def __init__(self, number, cvv):
        super(BankItauAccount, self).__init__(number)
        self.cvv = cvv
    
    def withdraw(self, value):
        self._BankBradescoAccount__total -= value
        self._BankBradescoAccount__total -= 2