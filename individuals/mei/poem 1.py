import random
import time
names=["Mei","She","He","It"]
place=["maze", "river","sky", "ocean","castle","physics class"]
verb=["play", "sleep", "drink", "sing","tear","throw", "swallow"]
thing=["poem", "dream", "xiao long bao", "langrande equation","cloud","python"]
#added a comment here
while 1:
    conclusion=random.random()
    
    if conclusion>0.9:
        print ("The"+"%s"%(random.choice(thing)+" is "+"%s"%(random.choice(verb)))+"ing")
    
    print ("%s"%(random.choice(names))+" stays in the "+"%s"%(random.choice(place)))
    print ("%s"%(random.choice(verb))+"ing "+"%s"%(random.choice(thing)))
    time.sleep(1)
    
