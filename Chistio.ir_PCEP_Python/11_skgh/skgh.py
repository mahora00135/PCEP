from random import randint
game = {
    's' : 'sang',
    'k' : 'kaghaz',
    'g' : 'gheychi',
}

player_score = 0
computer_score = 0
while True :
    i = input('sang(s), kaghaz(k), gheychi(g):')
    if i not in ['s','k','g']:
        print('not a valid input!')
        continue
    print('you choose ' + game[i])
    choices = ['s', 'k', 'g']  
    random_number = randint(0,2)
    c = choices[random_number]
    print('computer choose ' + game[c])
    if i == c :
        print('mosavi shod!')
    elif i == 's' :
        if c == 'k' :
            print('computer wins!')
            computer_score += 1
        else :
            print('you win1')
            player_score +=1
    elif i == 'k' :
        if c == 'g' :
            print('computer wins!')
            computer_score += 1
        else :
            print('you win!')
            player_score += 1
    elif i == 'g' :
        if c == 's' :
            print('computer wins!')
            computer_score += 1
        else :
            print('you win!')
            player_score += 1
    print('-----------------------------------')
    print('your total score : ' + str(player_score)) 
    print('computer total score : ' + str(computer_score))
    print('-----------------------------------')
    t = input ('continue? (y/n)')
    if t == 'y' :
        continue  # or pass
    elif t == 'n' :
        break