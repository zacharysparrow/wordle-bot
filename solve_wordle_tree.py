from utils import *
import time
import pickle
import multiprocessing

dict5 = []
with open('assets/words.txt') as f:
    for line in f:
        dict5.append(line.strip().split(',')[0])

class Node:
    def __init__(self, data, word):
        self.data = data
        self.word = word
        self.children = {}

    def add_child(self, child):
        self.children[child] = child

def tree_to_dict(node):
    if not node:
        return None

    tree_dict = {"data": node.data, "word": node.word}
    if node.children:
        tree_dict["children"] = {child.data: tree_to_dict(child) for child in node.children}
    
    return tree_dict

### build decision tree given word
def make_info_dict(dict5):
    return_dict = {i:{j:get_info(i,j) for j in dict5} for i in dict5}
    return return_dict

print("starting precomputation")
start_time = time.time()
info_lookup = make_info_dict(dict5)
end_time = time.time()
print(end_time - start_time)

def group_words(words):
    groups = {}
    for w in words:
        if w[1] in groups:
            groups[w[1]].append(w[0])
        else:
            groups[w[1]] = [w[0]]
    return groups

def build_tree(guess, word_list, level=0):
    word_info = [[w, info_lookup[guess.word][w]] for w in word_list]
    if len(word_info) == 1:
        new_node = Node('22222', None)
        guess.add_child(new_node)
        return None
    
    new_groups = group_words(word_info) 
    best_guesses = [(g, best_guess(dict5, new_groups[g], info_lookup)) for g in new_groups] #change dict5 to word_info[:,0] for hard mode
    for g,best in best_guesses:
        new_node = Node(g, best[0])
        guess.add_child(new_node)
        build_tree(new_node, new_groups[g], level=level+1)

def write_solution_tree(word):
    root = Node(None, word)
    build_tree(root, dict5)
    solution_tree = tree_to_dict(root)
    with open("data/trees/"+word+"_soln.pkl", "wb") as file:
        pickle.dump(solution_tree, file)
    print("finished "+word)
    
print("starting trees")
start_time = time.time()
start_words = dict5
num_processes = multiprocessing.cpu_count()
print(num_processes)
with multiprocessing.Pool(processes=num_processes) as pool:
    results = pool.map(write_solution_tree, start_words)

end_time = time.time()
print(end_time - start_time)
