from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for com in range(n):
        if not visited[com]:
            bfs(n, com, computers, visited)
            answer += 1
    return answer

def bfs(n, com, computers, visited):
    queue = deque()
    queue.append(com)
    visited[com] = True
    
    while queue:
        com = queue.popleft()
        for i in range(n):
            if not visited[i] and computers[com][i] == 1:
                queue.append(i)
                visited[i] = True