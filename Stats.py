import statistics
from statistics import mean 
from statistics import median
from collections import Counter
class Stats:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)

    def average(self):
        sum = 0
        for i in self.data:
            sum = sum + i
        return sum / self.count()

    def min(self):
        min = self.data[0]
        for i in range(len(self.data)):
            if(self.data[i] < min):
                min = self.data[i]
        return min
    
    def mean(self):
        return mean(self.data)
    
    def median(self):
        return median(self.data)
    
    def std(self):
        return statistics.stdev(self.data)

    def var(self):
        return statistics.pvariance(self.data)
    
    def freq_dist(self):
        '''d = {}
        for i in self.data:
            if d.get(i):
                d[i] +=1
            else:
                d[i] = 1
        return d'''
        return dict(Counter(self.data))

    def describe(self):
        print("Count : " , self.count())
        print("Min : " , self.min())    
        print("Average : " ,self.average())
        print("Mean :" , self.mean())
        print("Median :" , self.median())
        print("Std :" , self.std())
        print("Var :" , self.var())
        print("Freq :" , self.freq_dist())
        
    

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
s1 = Stats(ages)
s1.describe()

