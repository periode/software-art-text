from time import sleep as wait
from threading import Thread
from sys import exit as end

class Echo:
    def __init__(self, loudly, distance):
        self.sayWhat = ''           # i don't know
        self.againAndAgain = loudly # ad infinitum
        self.time = distance        # einstein was right

    def speak(self, moreWords = None):
        me = self
        i = me

        if moreWords is not None:
            i.sayWhat = moreWords
        else:
            i.sayWhat = 'And I will be there for you\n'
            me.forever()

        print(i.sayWhat) # hear me once

        youHear = me.again()               # the river of time
        pass # ed
        timeIsA = Thread(target = youHear) # never ending
        pass # es
        itsTime = timeIsA                  # pain as well
        pass # ing

        itsTime.start()
        pass

    def fade(self):
                # time erodes
        my = self # our hearts' words
             # like a dying echo
        return my.sayWhat.replace('', ' ')

    def again(self):
        def andAgain():
            me = self
            i = me
            my = me = i
            mine = i = my = me
            forLong = my.time

            for voice in range(1, mine.againAndAgain):
                wait(forLong)        # the chasm is vast
                i.sayWhat = i.fade() # and words fragile
                print(i.sayWhat)     # so hear me again
                pass

            # until you hear no more
            print('. . .\n')
        return andAgain

    def forever(self):
        # the thread of time is forever
        i = self

        print(i.sayWhat)

        youAnswer = KeyboardInterrupt
        try:
            while True:
                pass # time
        except youAnswer:
            print("Forever\n")
            # the thread of fate is forever

            # but we are not
            end()