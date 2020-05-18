import random, sys

print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins, lossess, and ties
wins=0
losses=0
ties=0

while True: #the main game loop
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True: #The player input loop
        print('Enter your move: (r)rock, (p)aper, (s)cissors or (q)uit')
        playerMove=input()
        if playerMove=='q':
            sys.exit() #quit the program
        if playerMove =='r' or playerMove =='p' or playerMove =='s':
            print("You've chose to exit the game")
            break #break out of input loop
        print('Type one of r, p, s, or q.')
    
    #Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    if playerMove == 'p':
        print('PAPER versus...')
    if playerMove == 's':
        print('SCISSORS versus...')

    #Display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    if randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
