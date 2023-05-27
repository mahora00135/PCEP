import sys

name = input('Please Enter Your Name :')
print('Hello ' + str(name))
word = 'chistio.ir'
turn = 10
guess = ''

while turn > 0 :
    i = input('Enter a Character :')
    if len(i) != 1 :
        print('pleas enter exactly \'one\' character')
        continue
    guess += i 
    if i not in word :
        turn -= 1
        print('Wrong!')
        print('You Have ' + str(turn) + ' Turn')
        
    win = True
    for c in word:
        if c in guess :
            sys.stdout.write(c)
        else:
            sys.stdout.write('_')
            win = False
        
        
    if win == True :
        print()
        print('Congradulation! You Win The Game!')
        break
        
     
        
if win == False:
    print()
    print('You Loose The Game')