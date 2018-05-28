import os
from flask import Flask, redirect, render_template, request

# creates the flask app.
app = Flask(__name__)

# --------------------------------------------- HOME PAGE



















if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)