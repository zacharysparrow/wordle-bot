from utils import *
#import seaborn as sns
#import matplotlib.pyplot as plt
import numpy as np
import json
import multiprocessing

dict5 = []
with open('assets/words.txt') as f:
    for line in f:
        dict5.append(line.strip().split(',')[0])

def compute_depth(solve_word):
    all_solns = []
    for word in dict5:
        soln = wordle_solve(word, solve_word)
        all_solns.append(soln)

    depths = []
    for soln in all_solns:
        depths.append(len(soln))

    soln_counts = dict(sorted(count_occurrences(depths).items()))
    return [solve_word, soln_counts]

num_processes = multiprocessing.cpu_count()
with multiprocessing.Pool(processes=num_processes) as pool:
    soln_hists = pool.map(compute_depth, dict5)

output_file = open('data/soln_step_lengths.json', 'w', encoding='utf-8')
for dic in soln_hists:
    json.dump(dic, output_file) 
    output_file.write("\n")

#print(soln_counts)
#
#mean_depth = np.mean(depths)
#
#plt.figure(figsize=(10, 6))
#hist = sns.histplot(data=depths, bins=6, discrete=True)
#y_bottom, y_top = hist.get_ylim()
#padding = (y_top - y_bottom) * 0.1
#hist.set_ylim(y_bottom, y_top + padding)
#text_place = np.mean(sorted(hist.get_yticks())[0:-1])
#
#plt.axvline(mean_depth, 0, 1, color='black')
#hist.annotate("mean: "+'{0:.2f}'.format(mean_depth), xy=(mean_depth + 0.1,text_place), horizontalalignment = 'center', rotation=270)
#for p in hist.patches:
#    number_label = int(p.get_height())/len(depths)
#    hist.annotate(
#        f'{number_label:.1%}',
#        (p.get_x() + p.get_width() / 2., p.get_height()),
#        ha='center',
#        va='center',
#        xytext=(0, 10),
#        textcoords='offset points'
#    )
#
#plt.title('Number of Guesses to Solve Wordle')
#plt.xlabel('# Guesses')
#plt.ylabel('Frequency')
#plt.grid(False)
#plt.show()
#
