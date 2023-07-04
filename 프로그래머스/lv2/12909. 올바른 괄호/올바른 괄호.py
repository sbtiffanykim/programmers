def solution(s):
    parenthesis = {')': '('}
    stack = []
    
    for c in s:
        if c not in parenthesis:
            stack.append(c)
        elif not stack or stack.pop() != parenthesis[c]:
            return False
        
    return len(stack) == 0