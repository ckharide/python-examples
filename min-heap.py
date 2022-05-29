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
    
    def pop(self):
        if(self.capacity < 1 ):
            print ("Heap underflow")
            return -1
        else:
            element = self.data[1]
            self.data[1] = self.data[self.capacity]
            self.capacity = self.capacity - 1 
            index = 1 
            leftchild = 2 * index
            rightchild = 2 * index + 1 
            while ( index < int (self.capacity / 2 )):
              if (self.data[index] > self.data[leftchild] or self.data[index] > self.data[rightchild]):
                if(self.data[leftchild] > self.data[rightchild]):
                    self.data[index] , self.data[leftchild] = self.data[leftchild] , self.data[index]
                    index = leftchild
                elif (self.data[index] > self.data[rightchild]):
                        self.data[index] , self.data[rightchild] = self.data[rightchild] , self.data[index]
                        index = rightchild
                else:
                      break
        return element


    
    def printHeap(self):
        for i in self.data:
            print(i)

minheap = Minheap(2)
minheap.push(4)
minheap.push(1)
minheap.push(2)

minheap.printHeap()
print(minheap.pop())




