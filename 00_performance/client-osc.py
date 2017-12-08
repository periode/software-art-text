
import socket

########### COMMUNICATION PART

ip = "127.0.0.1"
port = 2046

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))
print "listening for messages on port %i" % port



while True:
    data, address = sock.recvfrom(2046)
    order = data.decode('utf-8')
    print "...received message: %s" % order


########### SPEAKING PART

def onEnd(name, completed):
    print 'finishing', name, completed
    voice.endLoop()

def speak_out(w):
    voice = pyttsx.init()

    # for v in voice.getProperty('voices'):
    #     print 'voice %s' % v
    voice.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    voice.setProperty('volume', 0.6)

    rate = voice.getProperty('rate')

    voice.connect('finished-utterance', onEnd)
    voice.say(w)
    voice.runAndWait()
