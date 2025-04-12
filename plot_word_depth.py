import matplotlib.pyplot as plt

word_list = []
with open('data/word_depth.csv') as f:
    for line in f:
        word_list.append(line.strip().split(','))

depths = [int(w[1]) for w in word_list]

n_bins = 6
fig, axs = plt.subplots()
axs.hist(depths, bins=n_bins)

plt.show()
