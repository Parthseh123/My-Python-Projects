print("Riddle game \n You have 3 chances")
mode = input("Which mode do you want to play - Easy,Medium,Hard,Extreme - ")
mode = mode.lower()
Tries=0
loopact=0
while(loopact < 10):
    if(mode == "easy"):
        q1easy = input('1. What has four legs and a body but cannot walk ? \n')
        if("table" in q1easy):
            q2easy = input('2. What water can you eat and chew ? \n')
            q2easy=q2easy.lower
            if("watermelon" in q2easy):
                q3easy = input("3. I can be liquid or solid, sometimes I bubble and you can find me in every home. What am I? ")
                q3easy=q3easy.lower
                if("watermelon" in q2easy):
                    q4easy = input("4. Booming and zapping is what I can do, make sure to take cover so I won't get you. What am I? ")
                    q4easy=q4easy.lower
                    if("watermelon" in q2easy):
                        q5easy = input("5. Booming and zapping is what I can do, make sure to take cover so I won't get you. What am I? ")
                        q5easy=q5easy.lower

        else:
            while(Tries < 3):
                Tries+=1
                print("Wrong answer try again")
                q1easy = input('1. What has four legs and a body but cannot walk ? \n')
                if("table" in q1easy):
                    q2easy = input('2. What water can you eat and chew ? \n')
            print("Answer: Table")
            tries=0
            q2easy = input('2. What water can you eat and chew ? \n')
            q2easy=q2easy.lower
            if("watermelon" in q2easy):
                q3easy = input("3. I can be liquid or solid, sometimes I bubble and you can find me in every home. What am I? ")
