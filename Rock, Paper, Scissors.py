print("====ROCK, PAPER, SCISSORS GAME====")
player_1 = input("Player 1, input your name : ")
player_2 = input("Player 2, input your name : ")
print("Rules")
print("Rock : R   Paper : P   Scissors : S")
play_1 = input("Player One, Your Turn : ")
play_2 = input("Player Two, Your Turn : ")
if play_1.upper() == "R" and play_2.upper() == "R":
    print("Tie")
elif play_1.upper() == "R" and play_2.upper() == "P":
    print(player_2 + " wins")
elif play_1.upper() == "R" and play_2.upper() == "S":
    print(player_1 + " wins")
elif play_1.upper() == "P" and play_2.upper() == "P":
    print(player_1 + " tie")
elif play_1.upper() == "P" and play_2.upper() == "R":
    print(player_1 + " wins")
elif play_1.upper() == "P" and play_2.upper() == "S":
    print(player_2 + " wins")
elif play_1.upper() == "S" and play_2.upper() == "S":
    print(player_1 + "tie")
elif play_1.upper() == "S" and play_2.upper() == "P":
    print(player_1 + " wins")
elif play_1.upper() == "S" and play_2.upper() == "R":
    print(player_2 + " wins")
else :
    print("Error, Invalid Option")