import random
print("Stone paper scissor")
a=input("You will get 100 turns try to win all \n type 1 for stone 2 for scissor and type 3 for paper - ")
op = ["1","2","3"]
b= random.choice(op)

score=0
for i in range(100):
    if("1" in a and "3" in b):
        score=score-1
        print("you chose stone and computer chose paper \n computer won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("2" in a and "3" in b):
        score=score+1
        print("you chose scissor and computer chose paper \n you won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("3" in a and "3" in b):
        print("you chose paper and computer chose paper \n Draw")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("3" in a and "2" in b):
        score=score-1
        print("you chose paper and computer chose sissor \n computer won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("3" in a and "1" in b):
        score=score+1
        print("you chose paper and computer chose stone \n you won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
    elif("1" in a and "2" in b):
        score=score+1
        print("you chose stone and computer chose scissor \n you won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
    elif("1" in a and "1" in b):
        print("you chose stone and computer chose stone \n draw")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("2" in a and "1" in b):
        score=score-1
        print("you chose scissor and computer chose stone \n computer won")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)
        
    elif("2" in a and "2" in b):
        print("you chose scissor and computer chose scissor \n draw")
        print(score)
        a=input("type st for stone sc for scissor and type pa for paper - ")
        b= random.choice(op)



highscorer = open("highscore.txt","r")
data= int(highscorer.read())

if(score>data):
    score=str(score)
    highscore = open("highscore.txt","w")
    highscore.write(score)
    print('You cracked your highscore')
highscorew = open("highscore.txt","r")
data1= highscorew.read()
print("highscore:",data1)