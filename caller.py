import os
import sys
from random import randrange
import time

filename = "GameShowCallable"

def run(times, switch = 2):
	if (switch == 2):
		for x in range(times):
			door = randrange(3) +1
			switch = randrange(2)
			os.system('python %s.py %s %s' %(filename, door, switch))
	else:
		for x in range(times):
			door = randrange(3) +1
			os.system('python %s.py %s %s' %(filename, door, switch))


start = time.time()

try: #first argument defines how many times the loop iterates
    times = int(sys.argv[1])
except IndexError: #no arguments, the loop iterates one time
    times = 1

try: #second argument forces switching (0: no, 1: yes)
    switch = int(sys.argv[2])
    run(times, switch)
except IndexError: #no argument, the switching is random
    run(times)



end = time.time()
print(f"Time elapsed: {end - start}sec")