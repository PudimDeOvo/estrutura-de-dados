import LinkedStack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_last_but_one(head: Node) -> Node:
    if head is None or head.next is None:
        print("List has fewer than two nodes.")
        return None  

    current = head
    while current.next and current.next.next:
        current = current.next

    return current


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40) 

last_but_one = find_last_but_one(head)

if last_but_one:
    print(f"last but one: {last_but_one.data}") # output: 30
else:
    print("Found nothing :(")