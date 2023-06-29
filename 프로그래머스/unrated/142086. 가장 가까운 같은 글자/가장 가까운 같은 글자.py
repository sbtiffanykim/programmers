def solution(s):
    answer = []
    visited = dict()
    
    for idx, c in enumerate(s):
        if c not in visited:
            answer.append(-1)
        else:
            answer.append(idx - visited[c])
        visited[c] = idx            
    return answer