class Fight:
    def __init__(self, yelling, anger, argument, audience):
        self.yelling = yelling
        self.anger = anger
        self.argument = argument
        self.audience = audience

    def action(self):
        if (self.anger):
            print self.yelling
            if (self.argument):
                self.breakup()
        else:
            if (self.argument):
                self.breakup()
            else:
                resolution()

    def resolution(self):
        print self.audience + " sat with her lover happily on the porch."

    def breakup(self):
        print self.audience + " broke away from her lover's embrace."


jealousy = Fight("Where were you last night?", "You are never with me anymore", "jealousy", "woman")
jealousy.action()
