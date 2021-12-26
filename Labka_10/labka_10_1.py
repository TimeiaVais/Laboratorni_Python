class SetOfDigits:
    def __init__(self, a=0):
        self.a = a
    def NewElement(self):
        self.a = []
        self.el = (float(input('Write element:{0}'.format(i + 1))) for i in range(int(input('n ='))))
        self.a.append(self.el)
    def OutputSet(self):
        print(self.a)
    def FindMaxNum(self):
        max_num = max(self.a)
        return max_num
    def FindSumOfNums(self):
        suma = sum(self.a)
        return suma
set = SetOfDigits()
print(set.NewElement)
print(set.OutputSet)
print(set.FindSumOfNums)
print(set.FindMaxNum)