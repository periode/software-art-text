class Thought:
    def __init__(self,letters,meanings,audience):
        self.letters=letters
        self.meanings=meanings[0]
        self.hidden_meaning=meanings[1]
        self.audience=audience
    def happen(self):
        if (self.hidden_meaning):
            print self.audience
        else:
            print self.letters
maybe = Thought('We are', ['you','I'],'human')
maybe.happen()
        
    
        