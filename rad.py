import random

ch=str(input("Do you want to roll the dice? yes/no : "))

while ch=="yes":
    no=random.randint(1,6)
    if(no==1):
        print("[-------]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[-------]")
    if(no==2):
        print("[-------]")
        print("[       ]")
        print("[0     0]")
        print("[       ]")
        print("[-------]")
    if(no==3):
        print("[-------]")
        print("[0      ]")
        print("[   0   ]")
        print("[      0]")
        print("[-------]")
    if(no==4):
        print("[-------]")
        print("[0     0]")
        print("[       ]")
        print("[0     0]")
        print("[-------]")
    if(no==5):
        print("[-------]")
        print("[0     0]")
        print("[   0   ]")
        print("[0     0]")
        print("[-------]")
    if(no==6):
        print("[-------]")
        print("[0     0]")
        print("[0     0]")
        print("[0     0]")
        print("[-------]")

    ch=str(input("Do you want to roll the dice again? yes/no : "))

