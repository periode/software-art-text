import random
from time import sleep

pronouns = ['You', 'We', 'They']
noun = ['cluster', 'wave', 'collection', 'good source']
nouns = ['knowledge', 'wisdom', 'pride', 'hope', 'love']
verb = ['shines', 'perpetuates', 'revolves']
non = ['space', 'memory', 'air', 'light']

while True:
    print " %s are a %s of %s that %s in %s." % (random.choice(pronouns), random.choice(noun), random.choice(nouns), random.choice(verb), random.choice(non))
    sleep(5)