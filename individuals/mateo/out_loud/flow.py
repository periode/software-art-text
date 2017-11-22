# ==== | OUT/LOUD PERFORMANCE FLOW HELPERS | ====
import pyttsx3

def test():
    voices = pyttsx3.init()

    voices.say('oh my god')

    voices.runAndWait()

    print('huh')

def swapControl(name, completed, v1, v2, vCur):
    pass
