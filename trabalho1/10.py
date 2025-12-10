import ArrayStack

def get_precedence(op):
    precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return precedences.get(op, 0)

def tokenize(expression):
    tokens = []
    
    for op in ['+', '-', '*', '/', '^', '(', ')']:
        expression = expression.replace(op, f" {op} ")
        
    tokens = [t for t in expression.split() if t]
    return tokens


def infix_to_postfix(infix_expr) -> str: 
    stack = ArrayStack.ArrayStack()
    postfix_expr = []
    
    tokens = tokenize(infix_expr)
    
    for char in tokens: 
        
        if char.isalnum():
            postfix_expr.append(char)
            
        elif char == '(':
            stack.push(char)
            
        elif char == ')':
            while not stack._is_empty() and stack.peek() != '(':
                postfix_expr.append(stack.pop())
            
            if not stack._is_empty():
                 stack.pop()
            
        else:
            is_right_associative = char == '^' 
            
            while (not stack._is_empty() and
                   stack.peek() != '(' and
                   (get_precedence(stack.peek()) > get_precedence(char) or 
                    (get_precedence(stack.peek()) == get_precedence(char) and not is_right_associative))):
                
                postfix_expr.append(stack.pop())
            
            stack.push(char)
    
    while not stack._is_empty():
        postfix_expr.append(stack.pop())
    
    return ' '.join(postfix_expr)

def eval_postfix(postfix_expr) -> float:
    stack = ArrayStack.ArrayStack()
    
    for char in postfix_expr.split():
        if char.isdigit():
            stack.push(float(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            elif char == '^':
                result = operand1 ** operand2
            stack.push(result)
    
    return stack.pop()

def run_calculator(infix_expr) -> float:
    postfix_expr = infix_to_postfix(infix_expr)
    return eval_postfix(postfix_expr)

# 7
result = run_calculator("1 + 2 * 3")
print(result)

# 4
result = run_calculator("(10 + 2) / 3")
print(result)

# 11
result = run_calculator("5 * (4 - 2) + 1")
print(result)