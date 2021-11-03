import os
import sys
from random import randrange
import time

def run(times, switch = 2):
	if (switch == 2):
		for x in range(times):
			door = randrange(3) +1
			switch = randrange(2)
			os.system('python GameShowCallable.py %s %s' %(door, switch))
	else:
		for x in range(times):
			door = randrange(3) +1
			os.system('python GameShowCallable.py %s %s' %(door, switch))


start = time.time()

try:
    times = int(sys.argv[1])
except IndexError:
    times = 1

try:
    switch = int(sys.argv[2])
    run(times, switch)
except IndexError:
    run(times)



end = time.time()
print(f"Time elapsed: {end - start}sec")