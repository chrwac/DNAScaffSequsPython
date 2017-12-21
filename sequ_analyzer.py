class CSequAnalyzer:
    def __init__(self,sequence):
        self.__sequence = sequence
    def CountLetters(self):
        self.__lettercount = dict()
        for i in letters:
            self.__lettercount[i] = 0
        for i in self.__sequence:
            self.__lettercount[i]+=1
        self.__num_letters = sum(self.__lettercount.values())
    def PrintLetterCount(self):
        print(self.__num_letters)
        print(self.__lettercount)
    def PrintCGContent(self):
        self.__cgcontent=(float(self.__lettercount['C'])+float(self.__lettercount['G']))/float(self.__num_letters)
        print(self.__cgcontent)
    def Analyze(self):
        self.CountLetters()
        self.PrintLetterCount()
        self.PrintCGContent()