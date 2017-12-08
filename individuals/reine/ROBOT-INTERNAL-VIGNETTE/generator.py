import markov

print '/n'
print 'CREATIONISM'

text = open("./robot2.txt").read()
model = markov.build_model(text, 8)

print ''.join(markov.generate(model, 8))

text = open("./exist2.txt").read()
model = markov.build_model(text, 8)

print ''.join(markov.generate(model, 8))


text = open("./robot2.txt").read()
model = markov.build_model(text, 6)

print ''.join(markov.generate(model, 6))


text = open("./exist2.txt").read()
model = markov.build_model(text, 8)

print ''.join(markov.generate(model, 8))