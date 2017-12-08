import time

class Echo:
    def __init__(self, utterance, repetitions, distance):
        self.utterance = utterance
        self.repetitions = repetitions
        self.distance = distance

    def speak(self):
        for i in range(0, self.repetitions):
            yield self.utterance
            time.sleep(self.distance)
            self.utterance = self.utterance.replace('', ' ')

e = Echo('There is much to be said\nAnd even more to be heard', 3, 1)

for echo in e.speak():
    print(echo)
