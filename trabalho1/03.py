import ArrayStack

def transfer(S, T):
    """
    Transfers all elements from stack S to stack T.
    The order is reversed: the element that was on the top of S (first to leave) 
    goes to the base of T (first to enter), and vice-versa.
    
    O(n)
    """
    while not S._is_empty():
        
        element = S.pop()
        
        T.push(element)

S = ArrayStack.ArrayStack()
T = ArrayStack.ArrayStack()

S.push(10) 
S.push(20)
S.push(30) 
print(f"S before: {S.__str__()}") 
print(f"T before: {T.__str__()}") 

transfer(S, T)

print(f"S after: {S.__str__()}") 
print(f"T after: {T.__str__()}") 