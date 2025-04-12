import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

word_list = []
with open('word_depth.csv') as f:
    for line in f:
        word_list.append(line.strip().split(','))

depths = [int(w[1])+1 for w in word_list]

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
        xytext=(0, 10),  
        textcoords='offset points'  
    )

plt.title('Number of Guesses to Solve Wordle')
plt.xlabel('# Guesses')
plt.ylabel('Frequency')
plt.grid(False)
plt.show()

