import markov

text = open("./emma.txt").read()
model = markov.build_model(text, 8)

print ''.join(markov.generate(model, 8))
