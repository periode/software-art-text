# ====| CUT/UP - Flask Server |====
from flask import Flask, render_template, request, url_for, jsonify, redirect
import random
import time
#import pyttsx
import sys

app = Flask(__name__)
#voices = speech.getProperty('voices')

#voice_robot = random.choice(voices).id
#voice_phone = random.choice(voices).id

#while voice_robot == voice_phone:
#    voice_phone = random.chocie(voices).id

#print(voice_robot, voice_phone, file=sys.stderr, flush=True)
#print("what the fuck")

state = 'a'

content = {
    'a': {
        'robot': [],
        'calls': [],
        'poll': {
            'b': {
                'options': ['yay', 'keep it up!', 'you are great', 'keep going', 'stick with it', 'you are so good'],
                'count' : 0,
                'list' : []
                },
            'c': {
                'options':['no no no', 'stop', "don't waste your life", 'this is pointless', 'why are you doing this?', 'stupid robot'],
                'count' : 0,
                'list' : []
                }
            }
        },
    'b': {
        'robot': [],
        'calls': [],
        'poll': {
            'd': {
                'options':['you can do this', 'outgrow your shell!', 'no risk no gain', 'time to shine', 'do it!', 'believe yourself'],
                'count' : 0,
                'list' : []
                },
            'e': {
                'options':['stay in your comfort zone', 'what if you fail?', 'you could never...', "don't even think about it", 'are you mad?', 'you must be joking'],
                'count' : 0,
                'list' : []
                }
            }
        },
    'c': {
        'robot': [],
        'calls': [],
        'poll': {
            'e': {
                'options':['stay in your comfort zone', 'what if you fail?', 'you could never...', "don't even think about it", 'are you mad?', 'you must be joking'],
                'count' : 0,
                'list' : []
                },
            'f': {
                'options':['screw this!', "you'll find something better!", 'stop wasting your time and go!', 'this job is killing you', 'choose happiness!', 'you are built for greater things'],
                'count' : 0,
                'list' : []
                }
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
        choice = form['choice']
        word = form['word']
        print(word, choice)

        content[state]['poll'][choice]['count'] += 1
        lst = content[state]['poll'][choice]['list']
        lst.append(word)

        keys = []

        if time.clock() >= timestamp + 30:
            reset()
            p = content[state]['poll']

            for key in p:
                keys.append(key)

            if p[keys[0]]['count'] > p[keys[1]]['count']:
                state = keys[0]
            else:
                state = keys[1]
            timestamp = time.clock()
        
        keys = []
        p = content[state]['poll']
        for key in p:
            keys.append(key)
        
        n1 = p[keys[0]]['count']
        n2 = p[keys[1]]['count']
        print(n1, ':', n2)

    res = [] #[random.choice(wordsA), random.choice(wordsB)]
    
    pollObj = content[state]['poll']
    for item in pollObj:
        text = pollObj[item]['options']
        res.append({
            'key': item,
            'text': random.choice(text)
            })

    #res.append(random.choice(wordsA))
    #res.append(random.choice(wordsB))

    return jsonify(res)

@app.route('/api/reset')
def resetRoute():
    reset()
    return redirect('/')

@app.errorhandler(404)
def four_oh_four(err):
    return redirect('/')

def reset():
    timestamp = time.clock()
    
    for key in testPoll:
        element = testPoll[key]
        element['count'] = 0
        element['list'] = []

#print("stupid snek")   
#speech = pyttsx.init()


#if __name__ == '__main__':
#    app.run(host='10.225.87.183', port=5000)