from random import randrange
import time
import json
import ast
import os
import sys

doors = {  #id:[doorNum, hasPrize, wasChosen] - #wasChosen states: 0->no; 1->yes; 2->revealed by game
            0:[1,0,0],
            1:[2,0,0], 
            2:[3,0,0],
        }
doors[randrange(3)][1] = 1 #choose random prize door

filename = "output.txt"


def game(inp): #game start

    doors[inp-1][2] = 1 #set chosen door in dict

    for x in doors: #search for goat (and reveal to the player)
        if(doors[x][2] != 1):
            if(doors[x][1] != 1):
                doors[x][2] = 2
                break

    for x in doors: #search for unknown door (not choosen, and not revealed by game)
        if(doors[x][0] != inp and doors[x][2] != 2):
            unkn = x

    changed = int(sys.argv[2]) #CHANGE???

    if(changed==1):#change
        inp = doors[unkn][0]
        changed = 1
    else:#keep
        changed = 0

    for x in doors:#verify winning state
        if(doors[x][1] == 1):
            if(doors[x][0] == inp):
                print(f"Calling automated game script! {sys.argv[1]} {sys.argv[2]}, won")
                won = 1
            else:
                print(f"Calling automated game script! {sys.argv[1]} {sys.argv[2]}, lost")
                won = 0
            break

    #output to file
    dictOut = {
        0:doors[0],
        1:doors[1],
        2:doors[2],
        3:[0,0]
    }
    dictOut[3][0] = changed
    dictOut[3][1] = won
    
    with open(filename, "a") as f:
        dictStr = json.dumps(dictOut).replace('"', '')
        dictStr += '\n'
        f.write(dictStr)

    return dictStr
    #end

### MAIN
def main():
    game(int(sys.argv[1]))

main()
