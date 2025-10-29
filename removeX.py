class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.value, end=" → ")
        current = current.next
    print("NULL")

def remove_x(head, x):
    while head and head.value == x:
        head = head.next
    p = head
    while p and p.next:
        if p.next.value == x:
            p.next = p.next.next
        else:
            p = p.next
    return head

def remove_x(head, x):
    # remove ocorrências no início
    while head and head.value == x:
        head = head.next

    current = head
    while current and current.next:
        if current.next.value == x:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Entrada: 4 → 2 → 5 → 2 → 1 → NULL
head = create_linked_list([4, 2, 5, 2, 1])
print("Antes:")
print_list(head)

# x = 2
head = remove_x(head, 2)

print("Depois de remover 2:")
print_list(head)
