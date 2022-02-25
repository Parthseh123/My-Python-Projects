import random

a = random.randint(0,10)
yn = int(input(("Guess a number that is smaller than 10 and equall to computers number - ")))

b=1
while(b<10):
    if(a == yn):
        print("You guessed the write number !!")
        print("Next level")
        a = random.randint(0,100)
        yn = int(input(("Guess a number that is smaller than 100 and equall to computers number - ")))
        while(b<10):
            if(a == yn):
                print("You guessed the write number !!")
                print("Next level")
                a = random.randint(0,1000)
                yn = int(input(("Guess a number that is smaller than 1000 and equall to computers number - ")))
            while(b<10):
                if(a == yn):
                    print("You guessed the write number !!")
                    print("Next level")
                else:
                    print("You guessed the wrong one try again")    
                    yn = int(input(("Guess a number that is equall to computers number - ")))


    else:
        print("You guessed the wrong one try again")    
        yn = int(input(("Guess a number that is equall to computers number - ")))
        

