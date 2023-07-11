from collections import defaultdict



def solution(survey, choices):
    answer = ''    
    scores = {1: (3, 0), 2: (2, 0), 3: (1, 0), 4: (0, 0), 5: (0, 1), 6: (0, 2), 7: (0, 3)}
    types = defaultdict(int)
    
    for s, c in zip(survey, choices):
        # 비동의
        types[s[0]] += scores[c][0]
        # 동의
        types[s[1]] += scores[c][1]
        
    def compare(a, b):
        if types[a] >= types[b]:
            return a
        else:
            return b
        
    answer += compare('R', 'T')
    answer += compare('C', 'F')
    answer += compare('J', 'M')
    answer += compare('A', 'N')
    
    return answer