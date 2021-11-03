# Monty-Hall-Simulator
A python script to simulate the monty hall game show made by NotLatif

## What is the Monty Hall Problem
When presented with a choice (eg. three doors) where you have 1/3 chance of winning, if someone tells you one of the loosing doors and you switch, the chances of winning become 2/3
I recommend [this](https://www.youtube.com/watch?v=TVq2ivVpZgQ) video from D!NG to better understand it 

## How to use
There are three python files in the main directory:

.\GameShow!.py
This is the main script, it plays the game it has text responses and user input. Within the game you can also see statistics about previus games by entering S

.\GameShowCallable.py
This is the same code without user input, intended to be called by the called

.\caller.py
This script is a fast method to generate games, you can verify the outcome using the statistics function in the main script  
It calls the GameShowCallable script; it can accept 2 arguments

```batch
1:  number of iterations (0+)
2:  switch force (0=don't switch; 1=switch)
```
eg.
```batch
"caller.py"        REM this calls the game 1 time and the switch is random
"caller.py" 10     REM this calls the game 10 times and the switch is random
"caller.py" 100 1  REM this calls the game 100 times and forces it to switch
"caller.py" 100 0  REM this calls the game 100 times and forces it to not switch
```
