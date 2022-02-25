import random
print("Guess Yes or no and reach to the next level")
a=input("Guess Yes or no - ")
op = ["yes","no"]
b= random.choice(op)

i= 0
score=0
while score < 10:
    if(a == b):
        score=score+1
        print("You guessed it right")
        print("Score:",score)
        if(score == 10):
            break
        a=input("Guess Yes or no - ")
        b= random.choice(op)
    else:     
        print("You guessed it wrong")
        print("Score:",score)
        a=input("Guess Yes or no - ")
        b= random.choice(op)

print("Congratulations you Won this round lets go to the next round")
continuea = input("Do you wish to continue - ")
score=0

while score < 10:
    if("yes" in continuea):
        print("Level 2")
        print("If you guess wrong the score will become -1")
        a=input("Guess Yes or no - ")
        op = ["yes","no"]
        b= random.choice(op)
        while score < 10:
            if(a == b):
                score=score+1
                print("You guessed it right")
                print("Score:",score)
                if(score == 10):
                    break
                a=input("Guess Yes or no - ")
                b= random.choice(op)
            else:     
                score=score-1
                print("You guessed it wrong")
                print("Score:",score)
                a=input("Guess Yes or no - ")
                b= random.choice(op)
    else:
        exit()

print("Congratulations you Won this round lets go to the next round")
continuea = input("Do you wish to continue - ")

while score < 10:
    if("yes" in continuea):
        print("Level 3")
        print("Now you have to guess out of three")
        a=input("Guess Yes or no or either - ")
        op = ["yes","no","either"]
        b= random.choice(op)
        score=0
        while score < 10:
            if(a == b):
                score=score+1
                print("You guessed it right")
                print("Score:",score)
                if(score == 10):
                    break
                a=input("Guess Yes or no - ")
                b= random.choice(op)
            else:     
                score=score-1
                print("You guessed it wrong")
                print("Score:",score)
                a=input("Guess Yes or no - ")
                b= random.choice(op)
    else:
        exit()

print("Congratulations you Won this round lets go to the next round")
continuea = input("Do you wish to continue - ") 

while score < 10:
    if("yes" in continuea):
        print("Level 4")
        print("Now you have to guess out of four")
        a=input("Guess Yes or no or either or neither - ")
        op = ["yes","no","either","neither"]
        b= random.choice(op)
        score=0
        while score < 10:
            if(a == b):
                score=score+1
                print("You guessed it right")
                print("Score:",score)
                if(score == 10):
                    break
                a=input("Guess Yes or no - ")
                b= random.choice(op)
            else:     
                score=score-1
                print("You guessed it wrong")
                print("Score:",score)
                a=input("Guess Yes or no - ")
                b= random.choice(op)
    else:
        exit()

print("Congratulations you Won this round lets go to the next round")
continuea = input("Do you wish to continue - ") 

while score < 10:
    if("yes" in continuea):
        print("Level 5")
        print("Now you have to guess out of six")
        a=input("Guess '1' or '2' or '3' or '4' or '5' or '6' - ")
        op = ["yes","no","either","neither"]
        b= random.choice(op)
        score=0
        while score < 10:
            if(a == b):
                score=score+1
                print("You guessed it right")
                print("Score:",score)
                if(score == 10):
                    break
                a=input("Guess Yes or no - ")
                b= random.choice(op)
            else:     
                score=score-1
                print("You guessed it wrong")
                print("Score:",score)
                a=input("Guess Yes or no - ")
                b= random.choice(op)
    else:
        exit()