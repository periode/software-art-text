class Thought:
  def __init__(self, reality, imagination):
    self.reality = reality
    self.imagination = imagination

  def out(self):
    print self.reality



desire = Thought('i needed', 'i wanted')

desire.out()
