import random
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

N=5

player1=0
player2=0

for i in range (5):
    player1 += random.choice(dice1)
    player2 += random.choice(dice2)
    print(f"Dices: {player1/N} - {player2/N}")



if player1>player2:
    print("Player 1 Won! ")
elif player2>player1:
    print("Player 2 Won!")
else:
    print("Withdraw")



