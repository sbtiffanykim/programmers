import re

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        a = re.sub('aya', ' ', b)
        a = re.sub('ye', ' ', a)
        a = re.sub('woo', ' ', a)
        a = re.sub('ma', ' ', a)
        a = a.rstrip()
        if len(a) == 0: answer += 1
        
    return answer