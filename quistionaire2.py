import random
n = 0
while n < 10:
    option1 = input("Enter option 1 - ")
    option2 = input("Enter option 2 - ")

    l = [option1, option2]
    addornot = input("Do you want to add more - ")
    if("yes" in addornot or "add" in addornot):
        option3 = input("Enter option 3 - ")
        addornot = input("Do you want to add more - ")
        l.append(option3)
        if("yes" in addornot or "add" in addornot):
            option4 = input("Enter option 4 - ")
            addornot = input("Do you want to add more - ")
            l.append(option4)
            if("yes" in addornot or "add" in addornot):
                option5 = input("Enter option 5 - ")
                addornot = input("Do you want to add more - ")
                l.append(option5)
                if("yes" in addornot or "add" in addornot):
                    option6 = input("Enter option 6 - ")
                    addornot = input("Do you want to add more - ")
                    l.append(option6)
                    if("yes" in addornot or "add" in addornot):
                        option7 = input("Enter option 7 - ")
                        addornot = input("Do you want to add more - ")
                        l.append(option7)
                        if("yes" in addornot or "add" in addornot):
                            option8 = input("Enter option 8 - ")
                            addornot = input("Do you want to add more - ")
                            l.append(option8)
                            if("yes" in addornot or "add" in addornot):
                                option9 = input("Enter option 9 - ")
                                addornot = input("Do you want to add more - ")
                                l.append(option9)
                                if("yes" in addornot or "add" in addornot):
                                    option10 = input("Enter option 10 - ")
                                    addornot = input("Do you want to add more - ")
                                    l.append(option10)

    a = input("Enter any question that can be answered in yes or no you want to ask from god - ")
    an = random.choice(l)
    print(an)
