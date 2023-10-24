from collections import defaultdict

def solution(clothes):
    answer = 1
    count = defaultdict(int)
    for name, c in clothes:
        count[c] += 1
    
    for t, n in count.items():
        answer *= (n+1)  # 종류별 옷 개수와 안입는 경우 1개를 고려해 조합
    
    answer -= 1  # 모두 안입는 경우는 제외
    return answer