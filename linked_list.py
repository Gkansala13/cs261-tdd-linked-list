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
            self.prev=node

    def delete(self):
        self.next.prev=self.prev
        self.prev.next=self.next
        del self 

    def insert(self,new_node):
        self.next.prev = new_node
        new_node.prev = self
        new_node.next = self.next
        self.next = new_node
               
    def at(self, n):
        if (n==0):
            return self
        else:
            return self.next.at(n-1)

    def search(self, searched_value):
        if (searched_value==self.value):
            return self
        if (self.is_last()):
            return None
        else:
            return self.next.search(searched_value)
            
    def insert_in_order(self, new_node):
        node = self.prev
        if(node.is_sentinel()):
            node.insert(new_node)
        elif(new_node.value>node.value):
             node.insert(new_node)
        else:
            node.insert_in_order(new_node)


 



