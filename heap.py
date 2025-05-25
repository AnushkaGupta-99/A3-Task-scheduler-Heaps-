'''
Python Code to implement a heap with general comparison function
'''

from custom import Node
def compare_size_node(a,b):
    if a.key>=b.key:
        return False
    elif a.key<b.key:
        return True
def compare_size(a,b):
    if a>=b:
        return False
    elif a<b:
        return True

def compare_priority_and_id(a,b):
    if a.key>b.key:
        return False
    elif a.key<b.key:
        return True
    else:
        if a.value.id<b.value.id:
            return True
        else:
            return False

    
        

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
#the array is actually a node object sort of thing
#can i put a default comparator function 
    
    def __init__(self, comparison_function, init_array=[]):
        self.comparison_function=comparison_function
        self.array=list(init_array)
        if self.array:
            if isinstance(self.array[0], int):
                for i in range(len(init_array)):
                    self.array[i] = Node(self.array[i])
        #MADE CHANGE TO THIS BLOCK
        self.build_heap()
        
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        pass
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        #this value could be a node as well
        if isinstance(value, int):
            value = Node(value)
    
    # Append the Node object to the heap array
        self.array.append(value)
    
    # Perform the up_heap operation to maintain the heap property
        self.up_heap(len(self.array) - 1)
        '''if value is int:
            value1=Node(value)
            self.array.append(value1)
        else:
            self.array.append(value)
            self.up_heap(len(self.array) - 1)'''
            
        
        # Write your code here
        pass

    def extract_value(self):
        if not self.array:
            raise IndexError('Heap is empty')
        
        top_value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        if self.array:
            self.down_heap(0)
            
        return top_value.value
    
    def extract_full(self):
        if not self.array:
            raise IndexError('Heap is empty')
        
        top_value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        if self.array:
            self.down_heap(0)
            
        return top_value


    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        if not self.array:
            raise IndexError('Heap is empty')
        
        top_value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        if self.array:
            self.down_heap(0)
            
        return top_value.key

        
        # Write your code here
        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)

        '''
        if self.array:
            return self.array[0].key

        # Write your code here
        pass
    def left_child(self,i):
        return 2*i+1
    def right_child(self,i):
        return 2*i+2
    def parent(self,i):
        return (i-1)//2
    def has_left(self,i):
        return self.left_child(i)<len(self.array)
    def has_right(self,i):
        return self.right_child(i)<len(self.array)
    

    
    def build_heap(self):
        n=len(self.array)
        if n==0:
            pass
        else:
            for i in range(n//2 -1,-1,-1):
                self.down_heap(i)

    def up_heap(self,i):
        parent=self.parent(i)
        if (self.array[i].value is None or self.array[parent].value is None):
            if i>0 and self.comparison_function(self.array[i].key,self.array[parent].key):
                self.swap(i,parent)
                self.up_heap(parent)
        else:
            if i>0 and self.comparison_function(self.array[i],self.array[parent]):
                self.swap(i,parent)
                self.up_heap(parent)


    def swap(self,i,j):
        self.array[i],self.array[j]=self.array[j],self.array[i]

    
        


    def down_heap(self,i):
        if self.has_left(i):
            left=self.left_child(i)
            small_child=left
            if self.has_right(i):
                right=self.right_child(i)
                if (self.array[left].value is None or self.array[right].value is None) and self.comparison_function(self.array[right].key,self.array[left].key):
                    small_child=right
                elif (not(self.array[left].value is None or self.array[right].value is None)) and self.comparison_function(self.array[right],self.array[left]):
                    small_child=right
            if (self.array[small_child].value is None or self.array[i].value is None) and self.comparison_function(self.array[small_child].key,self.array[i].key) :
                self.swap(i,small_child)
                self.down_heap(small_child)
            elif not(self.array[small_child].value is None or self.array[i].value is None) and self.comparison_function(self.array[small_child],self.array[i]):
                self.swap(i,small_child)
                self.down_heap(small_child)

                     


            



        
    
    # You can add more functions if you want to

'''heap = Heap(compare_size,[])
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(6)
heap.insert(1)
heap.insert(8)
print("Initial heap:")
for i in heap.array:
    print(i.value,end=" ")

# Insert an element
heap.insert(3)
print("After insertion:")
for i in heap.array:
    print(i.value,end=" ")

# Extract the top element
extracted = heap.extract()
print("Extracted:", extracted)
print("Heap after extraction:")
for i in heap.array:
    print(i.value,end=" ")

# Check top element
print("Top element:", heap.top())
extracted = heap.extract()
print("Extracted:", extracted)
print("Heap after extraction:")
for i in heap.array:
    print(i.value,end=" ")

# Check top element
print("Top element:", heap.top())
extracted = heap.extract()
print("Extracted:", extracted)
print("Heap after extraction:")
for i in heap.array:
    print(i.value,end=" ")

print("Top element:", heap.top())
extracted = heap.extract()
print("Extracted:", extracted)
print("Heap after extraction:")
for i in heap.array:
    print(i.value,end=" ")

print("Top element:", heap.top())
extracted = heap.extract()
print("Extracted:", extracted)
print("Heap after extraction:")
for i in heap.array:
    print(i.value,end=" ")

print("Top element:", heap.top())
extracted = heap.extract()
print("Extracted:", extracted)
print("Heap after extraction:")
for i in heap.array:
    print(i.value,end=" ")'''



