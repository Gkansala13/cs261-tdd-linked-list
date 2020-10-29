# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Grayson Kansala

class LinkedList:
    def __init__(self, value=None):
        self.value=value
        self.next=self
        self.prev=self
        self.data=self

    def is_sentinel(self):
        return self.value==None
    
    def is_empty(self):
        if self.next !=self or self.prev != self:
            return False
        return True
    
    def is_last(self):
        return self.last().is_sentinel()
     
    def last(self):
        return self.prev
    
    def append(self, node):
        if(self.is_empty()):
            self.next=node
            self.prev=node
            node.prev=self
            node.next=self
        else:
            self.last().next=node
            node.prev=self.last()
            node.next=self























   
        
        

    
         