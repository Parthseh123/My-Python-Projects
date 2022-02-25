import random
print("Odd or Even game")
i = 0

while i < 10:
    odev=input("Enter odd or even - ")
    a=int(input("Enter your number - "))
    nl=[1,2,3,4,5,6,7,8,9,10]
    b=random.choice(nl)
    odevc=None
    if("odd" in odev):
        odevc="even"
        if("odd" in odev and a+b%2 == 0):
            print(f"You chose {a} computer chose {b}")
            print("You lose")
        if("odd" in odev and a+b%2 != 0):
            print(f"You chose {a} computer chose {b}")
            print("You win")


    elif("even" in odev):
        odevc="odd"

        if("even" in odev and a+b%2 == 0):
            print(f"You chose {a} computer chose {b}")
            print("You win")
        if("even" in odev and a+b%2 != 0):
            print(f"You chose {a} computer chose {b}")
            print("You lose")


