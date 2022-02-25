

import random


o=0

print("Try Your Luck")
print("If you get points between 99-100 you are very very lucky\n if you get points between 90-98 you are very lucky\n if you get points between 60-90 you are lucky \n if you get points between 40-60 you are a little lucky \n if you get points between 20-40 you are You are not really lucky \n if you get points between 0-30 you are unlucky")
while o < 10:
    a=input("Press enter if you want to start ")
    l=[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
    b=random.choice(l)
    print(b)
    if(b>98):
        print("You are very very lucky!!!😎😎😎😎😎😎😎😎")
    if(b>90 ):
        print("You are very lucky!!")
    if(b>60 and b<90):
        print("You are lucky!")
    if(b>40 and b<60):
        print("You are a little lucky 😭")
    if(b>20 and b<40):
        print("You are not really lucky 😭😭")
    if(b<20):
        print("You are unlucky 😭😭😭😭😭")