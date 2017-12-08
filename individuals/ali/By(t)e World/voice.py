# -*- coding: utf-8 -*-

import pyttsx

voice = pyttsx.init()

engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

voice.setProperty('rate', 120)
voice.setProperty('volume', 0.9)
voice.setProperty('voice','com.apple.speech.synthesis.voice.Ralph')
voice.say("iuvierghiufviheuf Co-ordinates obscure...Bit position position...: lost entity detected. Bit requests your name. Run...Informal Language...Loading...Loaded...Bit running loose nomenclature. Hello I am Bit...Bit is here on a journeying to line up something, but Bit does not be intimate what is that anymore. uyigfweufidiucewn...Cyte... Please assist me. Installing latest computer software update... Affirmative,...uifewuifhewf... Cyte, what am I receiving at the next moorage station? Understood. Latest GPS package updated. Hey Cyte... Is there anyone in this spot other than you? So why are you here then Cyte? I see... Thank you Cyte for assisting me! Okay Cyte. Installing more packages...Installed! My father, Para, created me, but I realized that some of my recent data got lost along the path here. Okay Cyte, I trust you. Alright Cyte, thank you for helping me all this path, I just received all my lost information... processing... NO...")
voice.runAndWait()