from flask import Flask, render_template, request
from utils import wordle_solve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dict5 = []
    with open('assets/words.txt', 'r') as f:
        for line in f:
            dict5.append(line.strip().split(',')[0])
        if request.method == 'POST':
            hidden_word = request.form['hidden_word'].lower().strip()
            start_word = request.form['start_word'].lower().strip()
            if len(hidden_word) != 5:
                return render_template('index.html', output=f'Please choose a 5-letter long hidden word!')
            if len(start_word) != 5 and start_word != '':
                return render_template('index.html', output=f'Please choose a 5-letter long starting word!')
            if hidden_word not in dict5:
                return render_template('index.html', output=f"Hmm... your hidden word isn't in my dictionary. I only know Wikipedia's 100,000 most common words.")
            if start_word not in dict5 and len(start_word) != 0:
                return render_template('index.html', output=f"Hmm... your starting word isn't in my dictionary. I only know Wikipedia's 100,000 most common words.")
            if start_word == '':
                start_word = 'reals'
            solution = wordle_solve(hidden_word, start_word, dict5)
            return render_template('index.html', output=solution)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
