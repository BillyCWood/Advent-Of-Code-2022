#ROCK - A; X
#PAPER - B; Y
#SCISSORS - C; Z


pointScoring = {
    "rock" : 1,
    "paper" : 2,
    "scissors":  3,
    "lost" : 0,
    "draw" : 3,
    "won" : 6
}


possibilities = {
    "A X" : "draw",
    "A Y" : "won",
    "A Z" : "lost",
    "B X" : "lost",
    "B Y" : "draw",
    "B Z" : "won",
    "C X" : "won",
    "C Y" : "lost",
    "C Z" : "draw"
}

shapes = {
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors"
}


def main():
    score = 0


    f = open("input2a.txt","r")

    for line in f:
        line = line.strip("\n")
        shape = line[2]
        score +=pointScoring[shapes[shape]]
        score += pointScoring[possibilities[line]]



    f.close


    print("Part 1 - "+ str(score))


main()