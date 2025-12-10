class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class DoublyLinkedBase(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def _is_empty(self):
        return self.size == 0
    
    def reverse(self):
        current = self.head
        prev = None
        self.tail = self.head  
        
        while current is not None:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node       
            
        self.head = prev  
        
def print_list(self):
    current = self.head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
def append(base, data):
    new_node = Node(data)
    if base._is_empty():
        base.head = new_node
        base.tail = new_node
    else:
        base.tail.next = new_node
        base.tail = new_node
    base.size += 1
    
list = DoublyLinkedBase()

append(list, 'A')
append(list, 'B')
append(list, 'C')

print("Original list:")
print_list(list)

list.reverse()
print("Reversed list:")
print_list(list)