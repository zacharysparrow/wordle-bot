# The Wordle Bot
Check out the app <a href="https://wordlebot.pythonanywhere.com/">here</a>!

This is a simple web app for solving NYT Wordle puzzles. Think of a hidden word and watch as Wordle Bot guesses it in 6 tries or less!

## About the Project
The algorithm is based on a simple min-max algorithm. The basic idea is this---with each guess, you want to maximize the minimum amount information received. 

The stack:
- python
- flask (for the web app)

The app is deployed using <a href="https://www.pythonanywhere.com/">Python Anywhere</a>. To run locally, clone this repo, install flask, and run app.py.

For a dictionary, I used the 5 letter words contained both in Wikipedia's list of 100,000 most common words and an English dictionary, resulting in 3103 possibilities. Some words are clearly missing (looking at you, "pesto"), but this seems to be a nice size to balance computation time and fun.

### Some Interesting Wordle Questions Answered
Each word is scored as a first guess in data/word_scores.csv (lower is better). Some of the best starting words are...
<details>
<summary>Spoiler warning</summary>
reals, aloes, tails, roles, and rates
</details>

The number of guesses for each word using this algorithm is recorded in data/word_depth.csv (zero indexing). Looks like every word is reached in 6 guesses with the optimal starting word!

## License
Distributed under the MIT license. See LICENSE.txt for more information.
