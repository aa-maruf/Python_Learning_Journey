# In the famous Rock Paper Scissor game - Rock wins against scissors, paper wins
# against rock, and scissors wins against paper.
# Write a python program that takes two user inputs and returns who wins the game.
# Sample Input:
# > Player 1: rock
# > Player 2: paper
# Sample Output:
# > Player 2 is the winner

player1 = input('Player1: ')
player2 = input('Player2: ')


if (player1 == 'rock' and player2 == 'scissors') :
    print('Player1 is the winner')
elif (player1 == 'rock' and player2 == 'paper') :
    print('Player2 is the winner')
elif (player1 == 'paper' and player2 == 'scissors') :
    print('Player2 is the winner')
elif(player1 == 'paper' and player2 == 'rock') :
    print('Player1 is the winner')
elif(player1 == 'scissors' and player2 == 'rock') :
    print('Player2 is the winner')
elif(player1 == 'scissors' and player2 == 'paper') :
    print('Player1 is the winner')
else :
    print('Draw!')
    
