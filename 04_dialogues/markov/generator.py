import markov

ngram = 3

text = open("./prince.txt").read()
model = markov.build_model(text, ngram)

print ''.join(markov.generate(model, ngram, None, 500))
