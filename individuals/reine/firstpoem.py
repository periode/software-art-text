import random 

from time import sleep 


actor_adj= ["exhausted", "worn", "happy","paranoid","skeptical"]
actor = ["a professor", "a creature","a monster","a angel","my soul","my best friend's cousin"]
world = ["heaven","hell","that garden with the poison oak","my home","my mind","a classroom","my father's thoughts"]
thought = ["melancholy","grief","ego","insecurity","existentialism","trauma"]
provoke = ["register","come up anymore","make sense","matter","make sense"]
verb = ["locked away","hiding","wrapped up","revelling"]



while True:
	print "	"
	print "I think he was %s, but I can't remember whether he was from %s, %s, or %s. It doesn't really %s, I was too %s and %s in %s. " % (random.choice(actor),random.choice(world),random.choice(world),random.choice(world),random.choice(provoke),random.choice(actor_adj),random.choice(verb),random.choice(thought))
	print "	"
	sleep(10)