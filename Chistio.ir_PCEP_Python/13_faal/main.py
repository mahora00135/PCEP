import os
__DIR__ = os.path.dirname(os.path.abspath(__file__))
i = input('Enter Your Birth Month (1-12): ')
if int (i) < 1 or int (i) > 12 :
    print('Your number is not a valid month')
else:
    f = open(__DIR__ + '/matn_faalha/' + str(i) + '.txt','r')
    m = f.read()
    print(m)