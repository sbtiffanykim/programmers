def solution(score):
    answer = [0] * len(score)
    
    avg_scores = [(i, (s[0]+s[1])/2) for i, s in enumerate(score)]
    avg_scores.sort(key=lambda x: x[1], reverse=True)
    avg_scores = dict(avg_scores)
    scores = set(avg_scores.values())
    scores = sorted(scores, reverse=True)
    
    rank = 1
    for score in scores:
        temp = [k for k, v in avg_scores.items() if v == score]
        for t in temp:
            answer[t] = rank
        rank += len(temp)
        
    return answer