from utils import *

dict5 = []
with open('assets/words.txt') as f:
    for line in f:
        dict5.append(line.strip().split(',')[0])

### compute best word
word_scores = [] 
for w in dict5:
    curr_score = calc_score(w,dict5)
    word_scores.append([w,curr_score])

with open("data/word_scores.csv", 'w') as f:
    for row in word_scores:
        f.write(','.join(map(str, row)) + '\n')

### can wordle always be solved with an optimial strategy?
def group_words(words):
    groups = {}
    for w in words:
        if w[1] in groups:
            groups[w[1]].append(w[0])
        else:
            groups[w[1]] = [w[0]]
    return groups

word_depth = {}
def traverse_tree(start_group, word_group, level=0):
    guess = best_guess(start_group, word_group)
    if guess[0] in word_depth: 
        prev_depth = word_depth[guess[0]]
        word_depth[guess[0]] = min([prev_depth, level])
    else:
        word_depth[guess[0]] = level
    word_info = scan_word(guess[0], word_group)
    if len(word_info) == 1:
        return None
    new_groups = group_words(word_info)
    for g in new_groups:
        traverse_tree(start_group, new_groups[g], level=level+1)

traverse_tree(dict5, dict5)
with open('data/word_depth.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in word_depth.items()]

