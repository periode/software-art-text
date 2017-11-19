import random 
import json
from time import sleep 


twenty = json.load(open('database-twenty-and.json'))
math = json.load(open('math.json'))

while True:
	print "	"
	print "Not that I care but %s %s" % (random.choice(twenty),random.choice(math))
	
	print "%s %s" % (random.choice(twenty),random.choice(math))
	
	
	
	print "	"
	sleep(10) 