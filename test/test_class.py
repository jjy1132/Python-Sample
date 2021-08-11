class Calculator:
    def __init__(self):
        self.val = 0

    def add(self,val):
        self.val += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.val -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
