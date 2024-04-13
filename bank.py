class BamkAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        if self.amt < 0:
            return "Your account, {}, is overdrawn.".format(self.name)
        else:
            return "Your account, {}, has a positive balance.".format(self.name)


t1 = BamkAccount("Bob", 100)
print(t1)
