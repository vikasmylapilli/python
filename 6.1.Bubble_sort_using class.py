class Bubble_sort():
    def __init__(self,data,count =0, sort = True):
        self.data = data
        self.count = count
        self.sort = sort

    def bubble_sort(self):  
        if len(self.data)-self.count == 1:
            return self.data      
                
        for i in range (1,len(self.data)-(self.count)):            
            if self.data[i-1] > self.data[i]:
                self.data[i-1],self.data[i] = self.data[i],self.data[i-1]
                self.sort =False
        self.count += 1
        if self.sort is True:
            return self.data         
        return self.bubble_sort()

    def print(self):
        for i in self.data:
            print(i,end=", ") 
        print("\n",self.count) 

      

if __name__=="__main__":
    elements = [1,2,3,4,5,6,7,8,9]
    sort = Bubble_sort(elements)
    sort.bubble_sort()
    sort.print()
    
