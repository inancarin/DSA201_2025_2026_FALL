from stack import Stack
from collections import deque

def evaluateExpression_withDeque(exp):
    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    stack = deque()
    for sym in exp:
        if sym in d.values(): # if sym is opening bracket
            stack.append(sym)
        elif sym in d: # if sym is closing brackets
            if not stack: # if stack is empty
                return False
            elif stack[-1] != d[sym]:
                return False
            else:
                stack.pop()
        else:
            return False
    
    if not stack:
        return True
    return False


def evaluateExpression(exp):
    d = {
        "]": "[",
        ")": "(",
        "}": "{"
    }

    stack = Stack()
    for sym in exp:
        if sym in d.values(): # if sym is opening bracket
            stack.push(sym)
        elif sym in d: # if sym is closing brackets
            if stack.isEmpty():
                return False
            elif stack.peek() != d[sym]:
                return False
            else:
                stack.pop()
        else:
            return False
    
    if stack.isEmpty():
        return True
    return False

exp = "((([{}])))()[]"
#res = evaluateExpression(exp)
res = evaluateExpression_withDeque(exp)
print(res)