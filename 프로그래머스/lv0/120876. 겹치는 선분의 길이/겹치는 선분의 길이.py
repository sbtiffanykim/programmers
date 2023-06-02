def solution(lines):
    answer = 0
        
    records = [set([]) for _ in range(200)]
    
    for idx, line in enumerate(lines):
        x1, x2 = line
        for n in range(x1, x2):
            records[n + 100].add(idx)
    
    for r in records:
        if len(r) > 1:
            answer += 1
    
    return answer