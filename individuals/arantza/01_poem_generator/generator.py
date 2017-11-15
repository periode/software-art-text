import random
from time import sleep
import sys

verbs = ["write", "listen", "travel", "sail", "rise", "fall"]
subjects = ["your", "his", "her", "my"]
abstract_nouns = ["love", "heartbreak", "faith", "despair", "voice", "silence"]
adjectives = ["bright", "dim", "colorful", "pale", "alive", "lifeless"]
nature_nouns = ["sun", "moon", "clouds", "sky", "ocean", "land"]
other = ["life", "death"]


while True:
	print "let me %s to %s %s" % (random.choice(verbs), random.choice(subjects), random.choice(abstract_nouns)) 
	print "that is as %s as the %s" % (random.choice(adjectives), random.choice(nature_nouns))
	sleep(3)

	conclusion = random.random()

	if conclusion > 0.6:
		print "there is no %s." % random.choice(other)
		exit()
	elif conclusion > 0.4:
		print "there is %s." % random.choice(other)
		exit()
	else:
		print ""

	sys.stdout.flush()
	sleep(3)

