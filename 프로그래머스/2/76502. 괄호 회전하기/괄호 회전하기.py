parenthesis = {'}': '{', ')': '(', ']': '['}

def is_valid(s):
    stack = list()

    flag = True
    for c in s:
        if c not in parenthesis:
            stack.append(c)
        else:
            if stack and parenthesis[c] == stack[-1]:
                stack.pop()
            else:
                flag = False

    if stack or not flag:
        return False
    return True


def solution(s):
    n = len(s)
    answer = 0
    
    for i in range(n):
        rotated_str = s
        if i > 0:
            rotated_str = s[i:] + s[:i]  # 왼쪽으로 회전
        if is_valid(rotated_str):  # 올바른 괄호 문자열이면
            answer += 1
            
    return answer