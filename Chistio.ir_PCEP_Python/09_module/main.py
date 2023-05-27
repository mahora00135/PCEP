from libs.AvgCalculator import AvgCalculator

y1 = int(input('please enter math score:'))
y2 = int(input('please enter physic score:'))
y3 = int(input('please enter chemistry score:'))

ac_class = AvgCalculator()
avg = ac_class.calculate(y1, y2, y3)
print(avg)



'''
from random import randrange
n = randrange(10, 20)
import random
n = random.random()
print(n)
'''


'''
class AvgCalculator:
    x1_c = 4
    x2_c = 3
    x3_c = 2
    
    def calculate(self, x1, x2, x3):
        sum = (x1 * self.x1_c) + (x2 * self.x2_c) + (x3 * self.x3_c)
        avg = sum / (self.x1_c + self.x2_c + self.x3_c)
        return avg
    
    
y1 = int(input('please enter math score:'))
y2 = int(input('please enter physic score:'))
y3 = int(input('please enter chemistry score:'))

ac_class = AvgCalculator()
avg = ac_class.calculate(y1, y2, y3)
print(avg)
'''










'''
x1 = int(input('please enter math score:'))
x2 = int(input('please enter physic score:'))
x3 = int(input('please enter chemistry score:'))
x1_c = 4
x2_c = 3
x3_c = 2
sum = (x1 * x1_c) + (x2 * x2_c) + (x3 * x3_c)
avg = sum / (x1_c + x2_c + x3_c)
print(avg)
'''