import random
from time import sleep

actor_adjectives = ['imperceptible', 'defiant', 'howling', 'subtle', 'eerie', 'cute']
actor = ['feline', 'cat', 'purr', 'claws', 'friend', 'crawler']
act = ['jumps', 'caresses', 'envelops', 'touches', 'reaches into', 'pets']
victim_adjectives = ['frightened', 'foolish', 'eager', 'loud', 'quiet', 'unconscious', 'wide-eyed']
victim = ['shadow', 'shiver', 'glimpse', 'crawl', 'sinner', 'saviour', 'hand', 'smile', 'cry']

while True:
    print "the %s %s %s the %s %s." % (random.choice(actor_adjectives), random.choice(actor), random.choice(act), random.choice(victim_adjectives), random.choice(victim))
    sleep(3)
