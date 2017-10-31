# Note: code is in Python 3!

import random
from time import sleep

characters = ["student", "dragon", "wizard", "thief", "psychopath"]
actions = ["wrote", "scorched", "typed", "hexed", "mugged", "laughed at"]
objects = ["code", "scroll", "love letter", "toad", "girl", "victim"]
actions2 = ["confused", "enchanted", "infatuated", "jumped on", "slapped", "screamed at"]

switch = True
lastchar = random.choice(characters)
lastact = random.choice(actions)
lastobj = random.choice(objects)

while True:
    print("some", lastchar, lastact, "the", lastobj)
    lastchar = lastobj
    if switch:
        lastact = random.choice(actions2)
        lastobj = random.choice(characters)
        switch = False
    else:
        lastact = random.choice(actions)
        lastobj = random.choice(objects)
        switch = True

    sleep(2)
    

