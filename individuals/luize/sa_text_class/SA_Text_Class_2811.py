# class Word:
# 	def __init__(self, material, meanings, audience):
# 		self.letters = material
# 		self.apparent_meaning = meanings[0]
# 		self.hidden_meaning = meanings[1]
# 		self.audience = audience
# 		self.realized = False

# 	def happen(self):
# 		if(self.hidden_meaning):
# 			print self.audience

# 		else:
# 			print self.letters

# serendipity = Word("serendipity", "chance encounter", "lovers")

# serendipity.happen()



class Si:
	def __init__(mark, your_name, reality, the_best, always_be_here):
		mark.knows = your_name
		mark.creates = reality
		mark.wishes = the_best
		mark.will = always_be_here
		mark.creep = False

	def happen(mark):
		if(mark.creates):
			print mark.creates

		else:
			print mark.knows

creeper = Si("creeper", "mark is a creeper", "mark is", "mark")

creeper.happen()
