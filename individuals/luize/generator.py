# name = "luize"

# print "my name is %s" %(name)

# import random
# from time import sleep

# names = ["luize", "lisa", "laura"]

# while True:
# 	print "my name is %s" %(random.choice(names))
# 	sleep(1)


import random
from time import sleep

adjectives = ['everlasting', 'blooming', 'disastrous', 'shameless']
doer = ['rick', 'maggie', 'student', 'hairdresser']
verb = ['praises', 'cries', 'stabs', 'cherishes']
noun = ['Richard Wagner', 'Lebanon', 'tornado', 'fire extinguisher']

while True:

	print "the %s %s %s %s." % (random.choice(adjectives), random.choice(doer), random.choice(verb), random.choice(noun))
	conclusion = random.random()
	if conclusion > 0.8:
		print "there is a %s." % random.choice(doer)
		exit()
	elif conclusion > 0.6:
		print "there is no %s." % random.choice(doer)
		exit()

	# print "my name is %s" %(random.choice(names))
	# sleep(1)
	sleep(3)
