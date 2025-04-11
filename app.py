from flask import Flask, render_template, request
from utils import wordle_solve

app = Flask(__name__)

def read_text_file(filepath):
    try:
        with open(filepath, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

@app.route('/', methods=['GET', 'POST'])
def index():
    dict5 = []
    with open('assets/words.txt', 'r') as f:
        for line in f:
            dict5.append(line.strip().split(',')[0])
        if request.method == 'POST':
            hidden_word = request.form['hidden_word']
            start_word = request.form['start_word']
            solution = wordle_solve(hidden_word, start_word, dict5)
            return render_template('index.html', output=f'The solution: {solution}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
