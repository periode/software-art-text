import random
from time import sleep

pronoun = ["I", "we", "you", "they"]
verbs = ["love", "hate", "desire", "despise", "crave", "fear"]
nouns_1 = ["acceptance", "union", "togetherness", "conviviality", "cohabitation"]
nouns_2 = ["rejection", "desolation", "being alone", "solipsism", "solitude"]

while True:
    print "%s %s %s" % (random.choice(pronoun), random.choice(verbs),
    random.choice(nouns_1))
    print "%s %s %s" %  (random.choice(pronoun), random.choice(verbs),
    random.choice(nouns_2))
    sleep(5)
