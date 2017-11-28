class theHumanCondition:
    def __init__(self, solitude):
        self.solitude = solitude
    def alone(self):
        print "Are we lone?"
        if solitude == True:
            print "yes, we are"
        else:
            print "No, we are not"


areWe = theHumanCondition('True')
print areWe.alone()
