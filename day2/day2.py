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

part_two_possibilities = {
    "A X" : "lost",
    "A Y" : "draw",
    "A Z" : "won",
    "B X" : "lost",
    "B Y" : "draw",
    "B Z" : "won",
    "C X" : "lost",
    "C Y" : "draw",
    "C Z" : "won"
}

shapes = {
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors",
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors"
}


def main():
    score = 0


    f = open("input2a.txt","r")
    """
    for line in f:
        line = line.strip("\n")
        shape = line[2]
        score +=pointScoring[shapes[shape]]
        score += pointScoring[possibilities[line]]
    """
    for line in f:
        line = line.strip("\n")
        score+=pointScoring[part_two_possibilities[line]]
        if(part_two_possibilities[line] == "draw"):
            score+=pointScoring[shapes[line[0]]]
        elif(part_two_possibilities[line] == "lost"):
            if(line[0] == "A"):
                score+=pointScoring["scissors"]
            elif(line[0] == "B"):
                score+=pointScoring["rock"]
            else:
                score+=pointScoring["paper"]
            
        else:
            if(line[0] == "A"):
                score+=pointScoring["paper"]
            elif(line[0] == "B"):
                score+=pointScoring["scissors"]
            else:
                score+=pointScoring["rock"]

    f.close()


    #print("Part 1 - "+ str(score))
    print("Part 2 - " + str(score))


main()