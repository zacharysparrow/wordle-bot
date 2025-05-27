from utils import *
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import json

dict5 = []
with open('assets/words.txt') as f:
    for line in f:
        dict5.append(line.strip().split(',')[0])

soln_depth_list = []
with open('data/soln_step_lengths.json', 'r') as file:
    for line in file:
        soln_depth_list.append(json.loads(line))

soln_depth_dict = {key: depth for key,depth in soln_depth_list}

mean_depths = {}
for w in dict5:
    depths_count = soln_depth_dict[w]

    depths_list = [([int(i)] * depths_count[i]) for i in depths_count]
    depths = []
    for d in depths_list:
        depths.extend(d)
    mean_depth = np.mean(depths)
    mean_depths[w] = mean_depth

best_worst_case_words = []
depth_7_words = []
six_size = len(dict5)
for w in dict5:
    depths_count = soln_depth_dict[w]
    if '7' in depths_count:
        depth_7_words.append(w)
    if '6' in depths_count:
        six_depth = depths_count['6']
        if six_depth == six_size:
            best_worst_case_words.append(w)
        if six_depth < six_size:
            six_size = six_depth
            best_worst_case_words = [w]

print("Best words by worst case")
for w in best_worst_case_words:
    print([w, soln_depth_dict[w], mean_depths[w]])

print("Best words on average")
words_by_mean_depth = sorted(mean_depths.items(), key=lambda item: item[1])
for w in words_by_mean_depth[0:10]:
    print([w[0], soln_depth_dict[w[0]], mean_depths[w[0]]])

print("Words that don't win")
print(str(len(depth_7_words))+" of "+str(len(dict5)))
for w in depth_7_words:
    print([w, soln_depth_dict[w], mean_depths[w]])

print("Worst words on average")
for w in words_by_mean_depth[-10:]:
    print([w[0], soln_depth_dict[w[0]], mean_depths[w[0]]])

plot_word = words_by_mean_depth[0][0]
depths_count = soln_depth_dict[plot_word]

depths_list = [([int(i)] * depths_count[i]) for i in depths_count]
depths = []
for d in depths_list:
    depths.extend(d)
mean_depth = np.mean(depths)

plt.figure(figsize=(10, 6))
hist = sns.histplot(data=depths, bins=6, discrete=True)
y_bottom, y_top = hist.get_ylim()
padding = (y_top - y_bottom) * 0.1
hist.set_ylim(y_bottom, y_top + padding)
text_place = np.mean(sorted(hist.get_yticks())[0:-1])

plt.axvline(mean_depth, 0, 1, color='black')
hist.annotate("mean: "+'{0:.2f}'.format(mean_depth), xy=(mean_depth + 0.1,text_place), horizontalalignment = 'center', rotation=270)
for p in hist.patches:
    number_label = int(p.get_height())/len(depths)
    hist.annotate(
        f'{number_label:.1%}',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='white', linewidth=0, pad=2),
        xytext=(0, 10),
        textcoords='offset points'
    )

plt.title("Guesses to Solve with 1st Word '"+plot_word+"'")
plt.xlabel('# Guesses')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()

plot_word = 'queue'
depths_count = soln_depth_dict[plot_word]

depths_list = [([int(i)] * depths_count[i]) for i in depths_count]
depths = []
for d in depths_list:
    depths.extend(d)
mean_depth = np.mean(depths)

plt.figure(figsize=(10, 6))
hist = sns.histplot(data=depths, bins=6, discrete=True)
y_bottom, y_top = hist.get_ylim()
padding = (y_top - y_bottom) * 0.1
hist.set_ylim(y_bottom, y_top + padding)
text_place = np.mean(sorted(hist.get_yticks())[0:-1])

plt.axvline(mean_depth, 0, 1, color='black')
hist.annotate("mean: "+'{0:.2f}'.format(mean_depth), xy=(mean_depth + 0.1,text_place), horizontalalignment = 'center', rotation=270)
for p in hist.patches:
    number_label = int(p.get_height())/len(depths)
    hist.annotate(
        f'{number_label:.1%}',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        bbox=dict(facecolor='white', alpha=0.9, edgecolor='white', linewidth=0, pad=2),
        xytext=(0, 10),
        textcoords='offset points'
    )

plt.title("Guesses to Solve with 1st Word '"+plot_word+"'")
plt.xlabel('# Guesses')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()
