class Betrayed:
	def _init_(self,worthlessness,meanings,friend,acquaintance):
		self.letters = worthlessness
		self.broken_smile = meanings[0]
		self.clenched_fist = meanings[1]
		self.audience = friend
		self.actually = acquaintance
		self.realized = False
	
		
	def happen(self):
		if(self.broken_smile):
			print self.audience
		else:
			print self.actually
			
			
alcohol = Betrayed("alcohol",[]"excuse for mistakes"],"we weren't that good of friends anyway")

alcohol.happen()
