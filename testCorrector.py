def readCorrectAnswers():
    correctAnswers = list()
    
    # read file with correct answers
    with open("correctAnswers.txt","r") as file:
        for line in file:
            correctAnswers.append(line.strip('\n'))
    
    return correctAnswers

def inputAnswers():
    answers = list()

    for i in range(len(readCorrectAnswers())):
        answers.append(input("Answer to question " + str(i+1) + ": "))
    
    return answers

def computeScores():
    # Scoring variables
    #score = 0
    correct = 0
    incorrect = 0
    blank = 0

    for answers, correctAnswers in zip(inputAnswers(), readCorrectAnswers()):

        if answers == correctAnswers:
            correct += 1
            #score = score + float(pointsForCorrect)
        elif answers == " " or answers == "":
            blank += 1
        elif answers != correctAnswers:
            incorrect += 1
            #score = score - float(penalty)

    # Compute results
    correctScore = correct * float(pointsForCorrect)
    deletedScore = incorrect * float(penalty)
    score = correctScore - deletedScore

    # Show results
    print("")
    print("Number of correct answers: " + str(correct))
    print("Number of failed answers: " + str(incorrect))
    print("Number of blank answers: " + str(blank))
    print("")
    print("SCORE: " + str(score))

if __name__ == "__main__":

    # scoring features
    pointsForCorrect = input("How counts any correct answer? ")
    penalty = input("Which is the penalty for wrong answer? ")

    computeScores()