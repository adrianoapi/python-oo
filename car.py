class Car:
    
    rodas = 4
    
    def __init__(self, name):
        #self.color = color
        #self.year = year
        #self.make = make
        self.name = name
    
    def drive(self):
        print('started ', self.name)
    
    @staticmethod
    def hello():
        print('Hello world!')

    @classmethod
    def show(cls):
        print(cls.rodas)