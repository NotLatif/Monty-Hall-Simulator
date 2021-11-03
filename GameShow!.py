from colorama import init
from random import randrange
import numpy as np
import time
import json
import ast
import os
import sys
init()

class col:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    RES = '\033[0m'

filename = "output.txt"

doors = { #id:[doorNum, hasPrize, wasChosen] - #wasChosen states: 0->no; 1->yes; 2->revealed by game
            0:[1,0,0],
            1:[2,0,0], 
            2:[3,0,0],
        }
doors[randrange(3)][1] = 1 #choose random prize door

def div(n, d): #return 0 if division by 0
    return n / d if d else 0

def stats(): #statistics
    count = 0
    data = []

    winTimesChanged = 0
    winTimesKept = 0
    lostTimesChanged=0
    lostTimesKept=0

    timesChanged = 0
    timesKept = 0

    totalWins = 0
    totalLooses = 0
    totalGames = 0


    with open(filename) as f:
        for line in f:
            data.append(ast.literal_eval(line.strip()))
            count += 1

    totalGames = len(data)

    for game in data:

        if(game[3][0]==1 and game[3][1]==1): #changed and won?
            winTimesChanged += 1
            timesChanged += 1
            totalWins += 1

        if(game[3][0]==1 and game[3][1]==0): #changed and lost?
            lostTimesChanged += 1
            timesChanged += 1
            totalLooses += 1

        if(game[3][0]==0 and game[3][1]==1): #kept and won?
            winTimesKept += 1
            timesKept += 1
            totalWins += 1

        if(game[3][0]==0 and game[3][1]==0): #kept and lost?
            lostTimesKept += 1
            timesKept += 1
            totalLooses += 1


    totalLooses = totalGames-totalWins

    print("Data:")
    print(f"The game was played {totalGames} times")#times/total
    print(f"The choice was changed {timesChanged} times ({(div(timesChanged, totalGames))*100}%), and kept {timesKept} times({(div(timesKept, totalGames))*100}%);")
    print(f"win rate: {totalWins} ({(div(totalWins, totalGames))*100}%); lost rate:{totalLooses} ({(div(totalLooses, totalGames))*100}%)")
    print('')
    print(f"times changed: {timesChanged} ({(div(timesChanged, totalGames))*100}%)")
    print(f"changed and won: {winTimesChanged} ({(div(winTimesChanged, timesChanged))*100}%)")
    print(f"changed and lost: {lostTimesChanged} ({(div(lostTimesChanged, timesChanged))*100}%)")
    print('')
    print(f"times kept: {timesKept} ({(div(timesKept, totalGames))*100}%)")
    print(f"kept and won: {winTimesKept} ({(div(winTimesKept, timesKept))*100}%)")
    print(f"kept and lost: {lostTimesKept} ({(div(lostTimesKept, timesKept))*100}%)")

    print(f"")



def game(inp): #game start

    doors[inp-1][2] = 1 #set chosen door in dict

    for x in doors: #search for goat and reveal to the player
        if(doors[x][2] != 1):
            if(doors[x][1] != 1):
                print(f"{col.CYAN}The door {doors[x][0]} has a goat!")
                doors[x][2] = 2
                goat = x
                
                break

    for x in doors: #search for unknown door (not choosen, and not revealed by game)
        if(doors[x][0] != inp and doors[x][2] != 2):
            unkn = x

    print('You can change the door!')
    print(f'You choose the door {inp}, do you want to change it with the door {doors[unkn][0]}? ')
    changed = input('Yes/No > ')  #do you change???

    if(changed=="Yes"):#change door
        inp = doors[unkn][0]
        changed = 1
    else:#keep door
        changed = 0

    print(f"{col.CYAN}The door with the prize is!!!!")
    time.sleep(1)  #SUSPENCE

    for x in doors: #verify winning state
        if(doors[x][1] == 1):
            print(f"Door {doors[x][0]}!")
            if(doors[x][0] == inp):
                print(f"{col.GREEN}Congratulations!!")
                won = 1
            else:
                print(f"{col.RED}Retry...")
                won = 0
            break

    #output to file adding id 3 for more data
    dictOut = {
        0:doors[0],
        1:doors[1],
        2:doors[2],
        3:[0,0] #[has_changed, has_won]
    }
    dictOut[3][0] = changed
    dictOut[3][1] = won

    #write to file
    with open(filename, "a") as f:
        dictStr = json.dumps(dictOut).replace('"', '')
        dictStr += '\n'
        f.write(dictStr)



### MAIN
def main():
    print(f"{col.CYAN}Hi, welcome to the game show! ")
    print(f"You'll be presented with 3 doors; behind one of them there are 1.000.000€, behind the other two there is a sheep")
    print(f"Choose a door!    /    You can enter [S] for statistics | [X] to exit")
    print(f"{col.GREEN} |1|   |2|   |3|{col.WARNING}")
    inp = input(">> ")

    if(inp == 'S'):
        stats()
    elif(inp == 'X'):
        exit()
    elif(inp == '1' or inp == '2' or inp == '3'):
        game(int(inp))

main()
