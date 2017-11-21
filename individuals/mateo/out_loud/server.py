# ====| CUT/UP - Flask Server |====

from flask import Flask, render_template, request, url_for, jsonify, redirect
import random
app = Flask(__name__)

wordsA = ['bomb', 'awesome', 'robot', 'dynamic', 'look', 'tech']
wordsB = ['flower', 'rabbit', 'bunny', 'magic', 'nature', 'sunshine']

testPoll = {
    '0' : {
        'count' : 0,
        'list' : []
        },
    '1' : {
        'count' : 0,
        'list' : []
        }
    }

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/api/', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        form = request.form
        index = str(form['index'])
        word = form['word']
        print(word)

        testPoll[index]['count'] += 1;
        lst = testPoll[index]['list']
        lst.append(word)

        print(testPoll['0']['count'], ':', testPoll['1']['count'])

    res = [random.choice(wordsA), random.choice(wordsB)]

    return jsonify(res)