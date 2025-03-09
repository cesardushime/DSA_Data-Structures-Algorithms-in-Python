def is_balanced(mystring):
    matching = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for bracket in mystring:
        if bracket in matching:  # Closing bracket
            if not stack or stack.pop() != matching[bracket]: 
                return False  # Mismatch or empty stack
        elif bracket in matching.values():  # Opening bracket
            stack.append(bracket)  # Push to stack

    return not stack  # Stack should be empty if balanced

# Test cases
print(is_balanced("({a+b})"))  # True
print(is_balanced("))((a+b}{"))  # False
print(is_balanced("((a+b))"))  # True
print(is_balanced("))"))  # False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # True
