import ArrayDeque, ArrayStack

def verify_palindrome(palindromes):
    deque = ArrayDeque.ArrayDeque()
    stack = ArrayStack.ArrayStack()

    for char in palindromes:
        if char.isalnum():  
            lower_char = char.lower()
            deque.add_last(lower_char)
            stack.push(lower_char)

    while not deque._is_empty() and not stack._is_empty():
        if deque.delete_first() != stack.pop():
            return False

    return True

palindrome1 = "level"
palindrome2 = "radar"
non_palindrome1 = "hello world"
non_palindrome1 = "estrutura de dados"

print(f"'{palindrome1}' {verify_palindrome(palindrome1)}")
print(f"'{palindrome2}' {verify_palindrome(palindrome2)}")
print(f"'{non_palindrome1}' {verify_palindrome(non_palindrome1)}")
print(f"'{non_palindrome1}' {verify_palindrome(non_palindrome1)}")