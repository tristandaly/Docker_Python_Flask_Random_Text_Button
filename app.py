import os
from flask import Flask, escape, request, render_template, send_from_directory
from nltk import sent_tokenize
from urllib import request
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = "https://www.gutenberg.org/files/61236/61236-0.txt"
    response = request.urlopen(url)
    raw = response.read().decode('utf8')
    sentence = sent_tokenize(raw)

    result = random.choice(sentence)
    return render_template("index.html", result=result)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')