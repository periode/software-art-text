# -*- coding: utf-8 -*-
#a virus called love: a virus duplicate itself from the host using the DNA of the host

import random

host="I never thought I could one day be writing you these words. My heart was so filled with love for you. This morning when I feeling so lonely, it was still my heart that pushed me into saying I love you  and, unfortunately, it is also my heart that is making me say we are through.Yes, my darling, this is the end for us, maybe because we were not patient enough to overcome a few small problems.maybe we weren not able to deal with each others sensibilities and we did not believe that poems that says between intention andgesture lies a distance.Yes, yes, it is true. There is a distance betweenintention and gesture because I know I have always wanted to make you happy, just as I know you also wanted to make me happy. Yet, by pure incompetence on both parties, we weren not able to realize this unfortunately. So, it is best we put an end to this love affair. I know we will always be close to each other. We will bump into each other in the samebars and other usual places, and, inevitably, our eyes will meet. Still, the tears I shed with you have dried out, and the source of those tears has been extinguished. Still today, you will find your name engraved on my heart, but I am trying hard to make it beat to a different pace, now that it will no longer have the sound of your voice to move it.Dear Alice all I want is for you to be very happy, and that you continue to have a life of projects and never ending successes. But Alice, never forget that LOVE is the most beautiful and rare thing there is and, sometimes, you have to be a little bit patient and endure a little bit of pain to reach it."
#host="Imagery analysis of North Korea's latest missile launch reveals a bigger, better rocket that's been domestically built.The US remains determined to stop North Korea from building a credible nuclear force, but it's looking like the only option left is military intervention.The US ambassador to the UN said the launch brings the US closer to war, but experts say the US might just have to accept North Korea as a nuclear state."

infected_host=host

nutrition=len(host)


virus_antigen_bank=["l","o","v","e"]

time=10

#infection start

print "Exposed host:"
print host
  
def infection(virus_antigen_bank,host,infected_host,nutrition,nutrition_left):  
    
    for j in range (nutrition_left):
        antigen=virus_antigen_bank[random.randint(0,3)]
        
        while True:
            potential_binding_target = [i for i, a in enumerate(infected_host) if a == antigen]
            if len(potential_binding_target)!=0:
                break
        
        antigen_binding_site=potential_binding_target[random.randint(0,len(potential_binding_target)-1)]

        
        
        if (antigen=="l"):
            infected_host = host[:(antigen_binding_site+1)] + 'o' + host[(antigen_binding_site+2):]
        if (antigen=="o"):
            infected_host = host[:(antigen_binding_site+1)] + 'v' + host[(antigen_binding_site+2):]
        if (antigen=="v"):
            infected_host = host[:(antigen_binding_site+1)] + 'e' + host[(antigen_binding_site+2):]
        if (antigen=="e"):
            infected_host = host[:(antigen_binding_site+1)] + 'l' + host[(antigen_binding_site+2):]
        
        host=infected_host
        nutrition=nutrition_left
    return infected_host
    return nutrition
    
  

for i in range (time):


    host=infected_host
    nutrition_left=nutrition/(i+1)
    infected_host=infection(virus_antigen_bank,host,infected_host,nutrition,nutrition_left)
    print "\n\n"
    print str(i+1)+" hour(s) after infection:"
    print infected_host
    
    
    
    




