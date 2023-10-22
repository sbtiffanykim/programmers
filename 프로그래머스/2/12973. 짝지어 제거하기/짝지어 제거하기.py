def solution(s):
    stack = list()
    
    # 문자열 길이만큼 반복
    for curr in s:
        # stack이 비어있거나 stack top이 현재 문자와 같지 않다면
        if not stack or stack[-1] != curr:
            # stack에 넣기
            stack.append(curr)
        # 아니라면 stack에서 top 빼기
        else:
            stack.pop()
    
    # stack에 문자가 남아있지 않으면 모두 제거 할 수 있으므로 1 반환
    return 1 if not stack else 0