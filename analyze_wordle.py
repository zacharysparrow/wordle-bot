from utils import *

dict5 = []
with open('assets/words.txt') as f:
    for line in f:
        dict5.append(line.strip().split(',')[0])

all_solns = []
for word in dict5:
    soln = wordle_solve('solve', 'reals')
    all_solns.append(soln)

print(all_solns[0:5])
