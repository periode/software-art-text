import pyttsx

voice = pyttsx.init()

voice.setProperty('rate', 130)
voice.setProperty('volume', 0.9)
voice.setProperty('voice','com.apple.speech.synthesis.voice.Victoria')
voice.say("hello, i am the slow voice of your computer")

voice.setProperty('rate', 180)
voice.setProperty('volume', 0.2)
voice.setProperty('voice','com.apple.speech.synthesis.voice.Ralph')
voice.say("hello, i am the slow voice of your computer")

voice.runAndWait()
