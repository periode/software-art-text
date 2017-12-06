# ====| OUT/LOUD - Flask Server |====

# TODO: HOW TO OSC IF IP ISN'T LOCALHHOST??????

from flask import Flask, render_template, request, url_for, jsonify, redirect
import random
import time
#import pyttsx
import sys
import socket

from pythonosc import osc_message_builder, udp_client, osc_bundle_builder

app = Flask(__name__)

ip = "127.0.0.1"
ip2 = "10.226.10.21"
ip3 = 'localhost'
port = 2046

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client = udp_client.UDPClient(ip3, port)

def sendSimple(msg):
    client.send_message("/test", msg.encode())
    print("send")

def sendMult(add, *msg):
    global client
    message = osc_message_builder.OscMessageBuilder(address=add)

    for elem in msg:
        print('Element:', elem)
        message.add_arg(elem)

    message = message.build()
    client.send(message)

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
            },
        'period': 90
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
            },
        'period': 90
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
            },
        'period': 90
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

timestamp = 0
period = 90;

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/api/poll/', methods=['GET', 'POST'])
def poll():
    global timestamp
    global period
    global state

    try:
        if request.method == 'POST':
            form = request.form
            choice = form['choice']
            word = form['word']
            print(word, choice)

            content[state]['poll'][choice]['count'] += 1
            lst = content[state]['poll'][choice]['list']
            lst.append(word)

            keys = []
            p = content[state]['poll']
            for key in p:
                keys.append(key)

            index = -1;
            if keys[0] == choice:
                index = 0
            elif keys[1] == choice:
                index = 1

            sendMult('/text', index, word)

            if time.clock() >= timestamp + period:
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


        res = []
    
        pollObj = content[state]['poll']
        for item in pollObj:
            text = pollObj[item]['options']
            vol = (time.clock()-timestamp)/period
            if vol > 1:
                vol = 1.0
            res.append({
                'key': item,
                'text': random.choice(text),
                'volume': vol
                })

        return jsonify(res)
    except KeyError:
        res = [{
            'key': '0',
            'text': 'Thank You',
            'volume': 0
            },{
            'key': '0',
            'text': 'Robot Has Decided',
            'volume': 0
            }]
        return jsonify(res)

@app.route('/api/override/', methods=['GET', 'POST'])
def override():
    global timestamp
    global period
    global state

    if request.method == 'POST':
        reset()
        ovr = int(request.form['override'])
        print(ovr)

        states = ['a', 'b', 'c', 'd', 'e', 'f']
        if ovr < 6:
            state = states[ovr]
        else:
            print('RING RING')

    jsUrl = url_for('static', filename='override.js')
    cssUrl = url_for('static', filename='style.css')
    oCssUrl = url_for('static', filename = 'override.css')
    saUrl = url_for('static', filename = 'superagent.js')

    return render_template("override.html", js=jsUrl, css = cssUrl, sa = saUrl, oCss = oCssUrl)

@app.route('/api/reset')
def resetRoute():
    reset()
    return redirect('/')

@app.errorhandler(404)
def four_oh_four(err):
    return redirect('/')

def reset():
    timestamp = time.clock()
    sendMult('/reset', 1)
    
    for key in content:
        try:
            pollThing = content[key]['poll']
            for option in pollThing:
                thing = pollThing[option]
                thing['count'] = 0
                thing['list'] = []
        except KeyError:
            continue