class Minheap:
    def __init__(self , capacity):
        self.capacity = 0
        self.data = []
        self.data.append(0)
        self.maxcapacity = capacity
    
    def push(self, element):
        self.capacity += 1 
        if(self.capacity > self.maxcapacity):
            print("Heap has oveflown")
            self.capacity -=1
        else:
            self.data.insert(self.capacity,element)
            index = self.capacity
            parentIndex = int (index / 2 )
            while(self.data[index] < self.data[parentIndex] and index > 1):
                self.data[index] , self.data[parentIndex] = self.data[parentIndex] ,self.data[index]
                index = parentIndex
                parentIndex = int (index / 2)
        print("Pushed element " , element)
    
    def printHeap(self):
        for i in self.data:
            print(i)

minheap = Minheap(10)
minheap.push(4)
minheap.push(1)
minheap.push(2)

minheap.printHeap()




