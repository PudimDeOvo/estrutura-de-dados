class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
def create_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values:
        current.next = Node(v)
        current = current.next
    return head
    
def print_list(head):
    current = head
    while current:
        print(current.value, end=" → ")
        current = current.next
    print("NULL")
    
def merge_sorted_lists(list1, list2):
    dummy = Node(0)  # nó auxiliar
    tail = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

        # liga o restante de uma das listas, se sobrar
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next
    
# Exemplo 1
lista1 = create_linked_list([1, 2, 4])
lista2 = create_linked_list([1, 3, 4])
print("Lista 1:")
print_list(lista1)
print("Lista 2:")
print_list(lista2)
print("Resultado:")
merged = merge_sorted_lists(lista1, lista2)
print_list(merged)

# Exemplo 2
print("\nExemplo 2:")
lista1 = create_linked_list([])
lista2 = create_linked_list([])
print_list(merge_sorted_lists(lista1, lista2))

# Exemplo 3
print("\nExemplo 3:")
lista1 = create_linked_list([])
lista2 = create_linked_list([0])
print_list(merge_sorted_lists(lista1, lista2))

    