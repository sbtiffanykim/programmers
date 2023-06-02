def solution(numlist, n):
    answer = []
    diff = [abs(num - n) for num in numlist]
    diff.sort()
    
    for d in diff:
        if (d+n) not in answer and (d+n) in numlist:
            answer.append((d+n))
        else:
            answer.append(abs(d-n))
        
    return answer