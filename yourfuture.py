import random


money=0
print("See your future")
print("This will telll you how much money will you get in future")



o=0


while o < 10:
    a=input("Press enter if you want to start ")
    l=[0,1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    b=random.choice(l)
    
    if(b==100):
        print("You will be the most richest person!!!🤑🤑💲💲💲💰💸💸💰💰🤑🤑💲💲💲🤑🤑💲💲💲🤑🤑💲💲💲🤑🤑💲💲💲")
        print(b,"Centillion")
    if(b==98 or b==99):
        print("You will be very very rich!!!🤑🤑💲💲💲💰💸💸💰💰")
        print(b,"Billion")
    if(b>90 and b<98 ):
        print("You are very Rich!!🤑🤑💲💲💲🤑🤑")
        print(b,"Million")
    if(b>60 and b<90):
        print("You are Rich")
        print(b,"Thousand")
    if(b>30 and b<60):
        print("You are a not poor still")
        print(b,"Hundred")
    if(b>3 and b<30):
        print("You are very poor")
        print(b)
    if(b==3 or b==2):
        print("You are homeless")
        print(0)
    if(b==0):
        print("You are the poorest in the world")
        print("-",100000000000000000000000000000000000000000)
        


    
