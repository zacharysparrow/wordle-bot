import pickle

def get_info(guess, soln):
    c1 = list(guess)
    c2 = list(soln)
    correctQ = [0,0,0,0,0]
    placeQ = [0,0,0,0,0]
    for i in range(5):
        if c1[i] == c2[i]:
            c2[i] = 0
            correctQ[i] = 2
    for i in range(5):
        for j in range(5):
            if c1[i] == c2[j]:
                c2[j]=0
                placeQ[i] = 1
    all_info = [correctQ, placeQ]
    all_info = [max(row) for row in zip(*all_info)]
    return ''.join(str(x) for x in all_info)

def count_occurrences(my_list):
    counts = {}
    for item in my_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

def calc_score(string, remain, info_mat=None): 
    if info_mat == None:
        all_info = [get_info(string,w) for w in remain]
    else:
        all_info = [info_mat[string][w] for w in remain]
    class_info = count_occurrences(all_info)
    return max(class_info.items(), key=lambda x: x[1])[1]

def best_guess(words, remain, info_mat=None):
    if len(remain) == 1:
        return [remain[0], 1]
    else:
        if info_mat != None:
            guess_scan = {i: calc_score(i, remain, info_mat=info_mat) for i in words}
        else:
            guess_scan = {i: calc_score(i, remain) for i in words}
        return min(guess_scan.items(), key=lambda x: x[1])

def wordle_solve(key, start):
    with open('data/trees/'+start+'_soln.pkl', 'rb') as file:
        wordle_tree = pickle.load(file) 

    curr_guess = wordle_tree['word']
    curr_tree = wordle_tree['children']
    guess_num = 1
    search_path = [curr_guess]
    while curr_guess != key and guess_num <= 6:
        curr_info = get_info(curr_guess, key)
        curr_guess = curr_tree[curr_info]['word']
        curr_tree = curr_tree[curr_info]['children']
        search_path.append(curr_guess)
        guess_num += 1
    return search_path

#def scan_word(string, remain):
#    all_info = []
#    for w in remain:
#        all_info.append([w,get_info(string,w)])
#    return all_info
#
#def update_list(string, remain, info):
#    possible_words = scan_word(string, remain)
#    return [word[0] for word in possible_words if word[1] == info]
#
#def wordle_solve(key, start, dict5):
#    remain = dict5
#    b_guess = start
#    i = 0
#    info = get_info(b_guess, key)
#    search_path = [[b_guess, info]]
#    remain = update_list(b_guess, remain, info)
#    while info != '22222' and i < 6:
#        b_guess, b_score = best_guess(dict5, remain)
#        info = get_info(b_guess, key)
#        search_path.append([b_guess, info])
#        if b_guess == key:
#            return search_path
#        remain = update_list(b_guess, remain, info)
#        i += 1
#    return search_path
