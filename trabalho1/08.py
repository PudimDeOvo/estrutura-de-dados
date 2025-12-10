import ArrayStack

def check_parentheses_balance(expression):
    stack = ArrayStack.ArrayStack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack._is_empty() or stack.pop() != matches[char]:
                return False

    return stack._is_empty()

exp1 = "((A + B) * C) / D"  
exp2 = "((A + B) / C"        
exp3 = "(A * B))) + C"       
exp4 = "(A + B) * (C / D)"   
exp5 = ")A + B("             

print(f"'{exp1}': {check_parentheses_balance(exp1)}")
print(f"'{exp2}': {check_parentheses_balance(exp2)}")
print(f"'{exp3}': {check_parentheses_balance(exp3)}")
print(f"'{exp4}': {check_parentheses_balance(exp4)}")
print(f"'{exp5}': {check_parentheses_balance(exp5)}")