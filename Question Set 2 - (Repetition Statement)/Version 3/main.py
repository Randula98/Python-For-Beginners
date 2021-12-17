maxScore = 0

#get the user input for number of players
noOfPlayers = input("Input the number of players : ")
noOfPlayers = int(noOfPlayers)

#get the details and score for each player
for i in range(noOfPlayers):
    total = 0
    print()
    playerNo = input("Input player number : ")

    for j in range(3):
        score = input("Input score " + str(j + 1) + " : ")
        score = int(score)
        total = total + score

    if (maxScore < total):
        maxScore = total
        maxPlayer = playerNo

    #display total score of the player
    print("Total Score : " + str(total))

print()
#display the player with the highest score
print("Player no : " + str(maxPlayer) + " go the highest score of " + str(maxScore))