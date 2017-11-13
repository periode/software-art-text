import pyttsx

voice = pyttsx.init()

#################################### DIFFERENT PARAMETERS
print "------------------"
voices = voice.getProperty('voices')
print "getting all voices"
for v in voices:
    print v

print "------------------"
print "current voice: %s" % voice.getProperty('voice')

print "------------------"
volume = voice.getProperty('volume')
print "volume: %s" % volume

print "------------------"
rate = voice.getProperty('rate')
print "rate: %s" % rate



#################################### DIFFERENT EVENTS
def onStart(name):
    print "started: %s!" % name

def onWord(name, location, length):
    print "current: %s | word position (in characters): %s | word length: %s" % (name, location, length)

def onEnd(name, completed):
    print "done: %s! (completely? %s)" % (name, completed)


#################################### SETTING UP AND READING
voice.setProperty('rate', 140)

voice.connect('started-utterance', onStart)
voice.connect('started-word', onWord)
voice.connect('finished-utterance', onEnd)

voice.say('hello, i am thee voice of manufactured electronics', 'greeting')
voice.runAndWait()
