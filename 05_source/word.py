class Word:
    def __init__(self, material, meanings, audience):
        self.letters = material
        self.apparent_meaning = meanings[0]
        self.hidden_meaning = meanings[1]
        self.audience = audience
        self.realized = False

    def happen(self):
        if(self.hidden_meaning):
            print self.audience
        else:
            print self.letters


serendipity = Word("serendipity", ["chance encounter"], "lovers")

serendipity.happen()
