# ====| CUT/UP - Flask Server |====
from flask import Flask, render_template, request, url_for, jsonify, redirect
import random
import time
import pyttsx
import sys

app = Flask(__name__)
#voices = speech.getProperty('voices')

#voice_robot = random.choice(voices).id
#voice_phone = random.choice(voices).id

#while voice_robot == voice_phone:
#    voice_phone = random.chocie(voices).id

#print(voice_robot, voice_phone, file=sys.stderr, flush=True)
#print("what the fuck")

state = 0

content = {
    'a': {
        'robot': [],
        'calls': [],
        'poll': {
            'b': [],
            'c': []
            }
        },
    'b': {
        'robot': [],
        'calls': [],
        'poll': {
            'd': [],
            'e': []
            }
        },
    'c': {
        'robot': [],
        'calls': [],
        'poll': {
            'e': [],
            'f': []
            }
        },
    'd': {
        'robot': [],
        'calls': []
        },
    'e': {
        'robot': [],
        'calls': []
        },
    'f': {
        'robot': [],
        'calls': []
        }
    }

wordsA = ['bomb', 'awesome', 'robot', 'dynamic', 'look', 'tech']
wordsB = ['flower', 'rabbit', 'bunny', 'magic', 'nature', 'sunshine']

wordsC = ['TEST', 'IS', 'SUCCESSFUL']
wordsD = ['THIS', 'WAS A', 'TRIUMPH']

timestamp = 0

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

@app.route('/api/poll/', methods=['GET', 'POST'])
def poll():
    global timestamp
    global state

    if request.method == 'POST':
        form = request.form
        index = str(form['index'])
        word = form['word']
        print(word)

        testPoll[index]['count'] += 1
        lst = testPoll[index]['list']
        lst.append(word)

        if time.clock() >= timestamp + 30:
            reset()
            state = 1
            timestamp = time.clock()

        print(testPoll['0']['count'], ':', testPoll['1']['count'])

    res = [] #[random.choice(wordsA), random.choice(wordsB)]
    
    if state == 0:
        res.append(random.choice(wordsA))
        res.append(random.choice(wordsB))
    elif state == 1:
        res.append(random.choice(wordsC))
        res.append(random.choice(wordsD))

    return jsonify(res)

@app.route('/api/reset')
def resetRoute():
    reset()
    res = { 'status' : 'success'}
    return jsonify(res)

@app.errorhandler(404)
def four_oh_four(err):
    return redirect('/')

def reset():
    timestamp = time.clock()
    
    for key in testPoll:
        element = testPoll[key]
        element['count'] = 0
        element['list'] = []

print("stupid snek")   
speech = pyttsx.init()


#if __name__ == '__main__':
#    app.run(host='10.225.87.183', port=5000)