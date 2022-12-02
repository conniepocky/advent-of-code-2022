f = open("input.txt", "r")

arr = f.read().split("\n")

score = 0

print(arr)

# The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. 

for i in arr:
    line = i.split(" ")
    opponentChoice = i[0]
    playerChoice = i[2] 

    if playerChoice == "X": #lose
        if opponentChoice == "A": 
            score += 3
        elif opponentChoice == "B": 
            score += 1
        elif opponentChoice == "C":
            score += 2
    elif playerChoice == "Y": #draw
        score += 3
        if opponentChoice == "A": 
            score += 1
        elif opponentChoice == "B":
            score += 2
        elif opponentChoice == "C":
            score += 3
    elif playerChoice == "Z": #win
        score += 6
        if opponentChoice == "A": 
            score += 2
        elif opponentChoice == "B":
            score += 3
        elif opponentChoice == "C":
            score += 1

    print(opponentChoice)
    print(playerChoice)

print(score)