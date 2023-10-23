from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    temp = 0
    while temp < k:
        temp += count[answer][1]
        answer += 1
    
    return answer