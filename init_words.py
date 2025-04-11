dict5 = []
with open('assets/words.txt') as f:
    for line in f:
        dict5.append(line.strip().split(',')[0])
