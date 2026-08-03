class Heap:
    def __init__(self):
        self.heap=[]
    def insert(self,val):
        self.heap.append(val)
        current_index=len(self.heap)-1
        self._heapify_up(current_index)
    def _heapify_up(self,index):
        while index > 0:
            parent_index=(index-1)//2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index] , self.heap[parent_index]=self.heap[parent_index],self.heap[index]
                index=parent_index
            else:
                break
    def display(self):
        print(self.heap)
if __name__=='__main__':
    my_heap=Heap()
    arr=[20,40,51,63,21,8]
    for i in arr:
        my_heap.insert(i)
    
    print("initial heap")
    my_heap.display()
    
    print("inserting 54")
    my_heap.insert(54)
    
    print("after inserting")
    my_heap.display()
    