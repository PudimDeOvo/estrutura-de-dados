import ArrayStack

def is_operand(char):
    return char.isalpha() or char.isdigit()

def prefix_to_infix(prefix_expr):
    stack = ArrayStack.ArrayStack()
    
    prefix_expr = prefix_expr[::-1]
    
    for char in prefix_expr:
        if is_operand(char):
            stack.push(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expr = f"({operand1} {char} {operand2})"
            stack.push(new_expr)
    
    return stack.pop()

def prefix_to_postfix(prefix_expr):
    stack = ArrayStack.ArrayStack()
    
    prefix_expr = prefix_expr[::-1]
    
    for char in prefix_expr:
        if is_operand(char):
            stack.push(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expr = f"{operand1} {operand2} {char}"
            stack.push(new_expr)
    
    return stack.pop()

# EXAMPLES

prefix_expr = "*+ABC"
print(f"Expressão Prefixada: {prefix_expr}")
print(f"Forma Infixada:    {prefix_to_infix(prefix_expr)}")
print(f"Forma Pós-fixada:  {prefix_to_postfix(prefix_expr)}")

prefix_expr_2 = "*-/ABCD"
print(f"Expressão Prefixada: {prefix_expr_2}")
print(f"Forma Infixada:    {prefix_to_infix(prefix_expr_2)}")
print(f"Forma Pós-fixada:  {prefix_to_postfix(prefix_expr_2)}")