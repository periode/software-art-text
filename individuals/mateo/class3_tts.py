import pyttsx

#def f_u_wrap(num):
#    def proxy(decorate):
#        def func(name, completed):
#           decorate(num)
#        return func
#    return proxy

#@f_u_wrap(num=9)
#def test(num):
#    print(num)
#    voice.endLoop()


#numbah = 9

#voice = pyttsx.init()

#voice.connect('finished-utterance', test)

#voice.say('hi my name is floop')

#a = voice.startLoop()

engine = pyttsx.init()
def onStart(name):
   print ('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
   #if name == 'fox':
    #  engine.say('What a lazy dog!', 'dog')
   if name == 'dog':
      engine.endLoop()
engine = pyttsx.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.', 'dog')
engine.startLoop()

