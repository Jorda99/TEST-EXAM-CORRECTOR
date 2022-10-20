def readCorrection():
    
    # read file with correct answers
    with open("correction.txt") as f:
        correction = f.readlines()
    
    return correction

def inputAnswers():
    answers = list()

    for i in range(len(readCorrection())-2):
        answers.append(input("Answer to question " + str(i+1) + ": "))
    
    return answers

def computeScores():
    # Scoring variables
    score = 0
    correct = 0
    incorrect = 0
    blank = 0

    correction = readCorrection()

    questionValue = float(correction.pop(0).rstrip())   
    penalty = float(correction.pop(0).rstrip())

    print("***********************")
    print("Question value = " + str(questionValue))
    print("penalty value = " + str(penalty))
    print("***********************")

    for answers, correctAnswers in zip(inputAnswers(), correction):

        if answers == correctAnswers.rstrip():
            correct += 1
            score = score + float(questionValue)
        elif answers == " " or answers == "":
            blank += 1
        elif answers != correctAnswers.rstrip():
            incorrect += 1
            score = score - float(penalty)

    # Show results
    print("")
    print("Number of correct answers: " + str(correct))
    print("Number of failed answers: " + str(incorrect))
    print("Number of blank answers: " + str(blank))
    print("")
    print("FINAL SCORE: " + str(score))

if __name__ == "__main__":

    computeScores()