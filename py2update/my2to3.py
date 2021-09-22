#!/usr/bin/env python3

thisround = 0
while(True):
    print("what is the ip address used for broadcast? ")
    answer = input()
    thisround = thisround + 1
    if(answer == "255.255.255.255"):
        print("correct")
        break
    elif(thisround == 3):
        print("sorry")
        break
    else:
        print("try again")
