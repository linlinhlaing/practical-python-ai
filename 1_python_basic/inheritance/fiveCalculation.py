# coding: utf-8
#fivecalculation.py
from fiveCalculation import fourCalculation
class FiveCalculation(FourCalculation):
    """Adding power calculation"""
    def __init__(self, first, second,third):
        super().__init__(first, second)
        self.third = third
    def pow(self):
        return self.third ** 2

    def div(self):
        print("\nThis is overriding method")
        if self.second == 0: #Method overriding
            return 0
        else:
            return self.first/self.second    

d = FiveCalculation(10,5,3)
print(f'First number is {d.first}') 
print(f'Second number is {d.second}')
print(f'Addition result is {d.add()}') 
print(f'Second number is {d.second}')
print(f'Substraction result is {d.substract()}') 
print(f'Second number is {d.second}')
print(f'Multiplication result is {d.mul()}')     
print(f'Division result is {d.div()}')  
print(f'Power {d.pow()}')

