#### import markov.py file ####
import markov

#### read from life and death dataset ####
life_text = open("./life_dataset.txt").read()
death_text = open("./death_dataset.txt").read()

amount = 5;

life_model = markov.build_model(life_text, amount)
death_model = markov.build_model(death_text, amount)

print
print 'LIFE'
print ''.join(markov.generate(life_model, amount))
print
print 'DEATH'
print ''.join(markov.generate(death_model, amount))
