import os
from flask import Flask, redirect, render_template, request
from string import ascii_uppercase
from random import choice


# creates the flask app.
app = Flask(__name__)


# ----------------------------------------------------- VARIABLES



# ----------------------------------------------------- HOME PAGE
@app.route("/")
def landing_page():
    return render_template('index.html')

# ----------------------------------------------------- PLAYER NAME and REDIRECT TO PLAYER PAGE
@app.route("/login")
def get_username():
    username = request.args.get('user')
    return redirect(username)
    
@app.route("/<username>")
def user_game_page(username):
    return render_template('wordguess.html')


# ----------------------------------------------------- GUESSING LETTER
@app.route("/<username>/letter_guess")
def add_letter():
    hg
    



# ----------------------------------------------------- FUNCTIONS
# read in words file and create words list

def read_words_file(filename):
    f = open(filename)
    text = f.read().upper()
    words = text.splitlines()
    f.close()
    return words 

ALL_WORDS = read_words_file('words.txt')
WORD = choice(ALL_WORDS)












if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)