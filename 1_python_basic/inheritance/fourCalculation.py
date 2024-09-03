# coding: utf-8
#fourCalculation.py
"""A simple class creatin for arithmetic operation"""
class FourCalculation:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second

    def substract(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first/self.second
    
a = FourCalculation(10,5)
print(f'First number is {a.first}') 
print(f'Second number is {a.second}')
print(f'Addition result is {a.add()}') 
print(f'Second number is {a.second}')
print(f'Substraction result is {a.substract()}') 
print(f'Second number is {a.second}')
print(f'Multiplication result is {a.mul()}')     
print(f'Division result is {a.div()}')  
