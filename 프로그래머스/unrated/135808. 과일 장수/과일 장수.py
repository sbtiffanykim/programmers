def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for idx in range(0, len(score) , m):
        temp = score[idx:idx+m]
        if len(temp) == m:
            min_score = min(temp)
            answer += min_score * m

    return answer