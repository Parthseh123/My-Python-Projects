Username = "Parth"
diarynickname = "DiBuddy"
password = "p"
n=0

diary_code = {}

def addorsee():
    add_or_see = input("Do you want to add or see - ")
    while(n < 10):
        if("add" in add_or_see):
            addpgnum = int(input("Enter you Page number - "))
            add1page=input("Enter your text - ")
            
            diary_code.update({addpgnum : add1page})
            add_or_see = input("Do you want to add or see - ")

        if("see" in add_or_see):
            pgnumber=int(input("Enter the page number you want to see - "))
            print(diary_code[pgnumber])
            add_or_see = input("Do you want to add or see - ")


                

open = input("Enter The password to open the diary - ")
if(open == password):
        addorsee()    
else:
    print("try again")
    open = input("Enter The password to open the diary - ")
    if(open == password):
        addorsee()    
    else:
        print("try again")
        open = input("Enter The password to open the diary - ")
        if(open == password):
            addorsee()
        else:
            print("Diary Locked")






