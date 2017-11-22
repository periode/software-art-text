#### import markov.py file ####
import markov

#### read from life and death dataset ####
life_text = open("./life_dataset.txt").read()
death_text = open("./death_dataset.txt").read()

life_model = markov.build_model(life_text, 5)
death_model = markov.build_model(death_text, 5)

print
print 'LIFE'
print ''.join(markov.generate(life_model, 5))
print
print 'DEATH'
print ''.join(markov.generate(death_model, 5))
