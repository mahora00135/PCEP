from random import randomrange
number = randrage(0, 100)
has_guesses = False


while has_guesses == False:     #True
    i = int(input('Enter a number:'))
    if i == number :
        print('Ok! the number is ' + str(i))
        has_guesses = True      #break
    elif i < number:
        print('your number is lower than our number')
    else:
        print('your number is greater than our number')