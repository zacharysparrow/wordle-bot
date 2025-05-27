# The Wordle Bot
Check out the app <a href="https://wordlebot.pythonanywhere.com/">here</a>!

This is a simple web app for solving NYT Wordle puzzles. Think of a hidden word and watch as Wordle Bot guesses it in 6 tries or less!

## About the Project
The algorithm is based on a simple min-max algorithm. The basic idea is this---with each guess, you want to maximize the minimum amount information received. 

The stack:
- python
- flask (for the web app)

For plotting:
- numpy
- Matplotlib
- seaborn

The app is hosted on <a href="https://www.pythonanywhere.com/">Python Anywhere</a>.

For a dictionary, I used the 5 letter words contained both in Wikipedia's list of 100,000 most common words and an English dictionary, resulting in 3103 possibilities. Some words are clearly missing (looking at you, "pesto"), but this seems to be a nice size to balance computation time and fun.

Find a brief analysis of the best and worst starting words on <a href="zacharysparrow.github.io/projects/the_wordle_bot/">my website</a>.

## License
Distributed under the MIT license. See LICENSE.txt for more information.

## Disclaimer
This repository is not affiliated with the official Wordle site or the New York Times.
