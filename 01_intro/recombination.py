import sys
import random
from time import sleep

actor_adjectives = ['imperceptible', 'defiant', 'howling', 'subtle', 'eerie', 'cute']
actor = ['feline', 'cat', 'purr', 'claws', 'friend', 'crawler']
act = ['jumps', 'caresses', 'envelops', 'touches', 'reaches into', 'pets']
victim_adjectives = ['frightened', 'foolish', 'eager', 'loud', 'quiet', 'unconscious', 'wide-eyed']
victim = ['shadow', 'shiver', 'glimpse', 'crawl', 'sinner', 'saviour', 'hand', 'smile', 'cry']

def pickRandomNumber():
    return random.random()

while True:
    print "the %s %s %s the %s." % (random.choice(actor_adjectives), random.choice(actor), random.choice(act), random.choice(victim_adjectives)),

    conclusion = pickRandomNumber()

    if conclusion > 0.85:
        print ""
        sleep(1)
        print ""
        sleep(1)
        print "there is a %s." % random.choice(victim)
        exit()
    elif conclusion > 0.7:
        print ""
        sleep(1)
        print ""
        sleep(1)
        print "there is no %s." % random.choice(victim)
        exit()

    sys.stdout.flush()

    sleep(3)
