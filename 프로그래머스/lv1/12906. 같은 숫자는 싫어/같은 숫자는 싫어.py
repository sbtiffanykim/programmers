from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]
    while len(arr) > 0:
        num = arr.popleft()
        if num != answer[-1]:
            answer.append(num)
    return answer