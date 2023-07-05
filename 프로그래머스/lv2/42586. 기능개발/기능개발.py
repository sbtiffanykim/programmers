from collections import deque

def get_queue(progresses, speeds):
    q = deque()
    
    for p, s in zip(progresses, speeds):
        n, r = divmod((100 - p), s)
        if r != 0: 
            q.append(n+1)
        else:
            q.append(n)
    return q

def solution(progresses, speeds):
    answer = []
    q = get_queue(progresses, speeds)
    cnt = 1
    curr = q.popleft()
    
    while q:
        val = q.popleft()
        if curr >= val:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            curr = val
    answer.append(cnt)
    
    return answer